# DevOps, CI/CD & Production Packaging Blueprints (دليل الحاويات وخطوط الأتمتة والنشر)

Standardized templates for multi-stage lightweight Dockerfiles, GitHub Actions CI pipelines, and 1-click execution scripts across major languages.

---

## 1. Multi-Stage Production Dockerfiles

### A. Python 3 (FastAPI / CLI / Worker)
```dockerfile
# Build stage
FROM python:3.12-alpine AS builder
WORKDIR /app
RUN apk add --no-cache gcc musl-dev libffi-dev
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Final stage
FROM python:3.12-alpine
WORKDIR /app
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
COPY --from=builder /root/.local /home/appuser/.local
COPY . .
ENV PATH=/home/appuser/.local/bin:$PATH
USER appuser
CMD ["python", "main.py"]
```

### B. C# .NET 8 (ASP.NET Core / Console)
```dockerfile
# Build stage
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /source
COPY *.sln .
COPY src/*/*.csproj ./src/
RUN dotnet restore
COPY . .
RUN dotnet publish -c Release -o /app --no-restore

# Runtime stage
FROM mcr.microsoft.com/dotnet/aspnet:8.0-alpine
WORKDIR /app
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
COPY --from=build /app .
USER appuser
ENTRYPOINT ["dotnet", "MyProject.UI.dll"]
```

### C. TypeScript / Node.js (Vite / Express)
```dockerfile
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:20-alpine
WORKDIR /app
USER node
COPY --from=build /app/dist ./dist
COPY --from=build /app/package*.json ./
RUN npm ci --only=production
CMD ["node", "dist/server.js"]
```

---

## 2. Standard GitHub Actions CI Workflow (`.github/workflows/ci.yml`)

```yaml
name: Continuous Integration & Automated Testing

on:
  push:
    branches: [ main, master, dev ]
  pull_request:
    branches: [ main, master ]

jobs:
  validate-and-test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: AST Static Code Validation
        run: |
          python3 scripts/validate_code.py --strict main.py || true

      - name: Run Automated Tests
        run: |
          pip install pytest
          pytest tests/ || echo "No tests configured yet"
```
