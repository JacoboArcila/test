
# Prueba Técnica (Resuelta) — Python + React + TailwindCSS + SQLite

## Backend
- **Stack:** FastAPI + SQLite
- **Endpoints:**
  - `GET /products` → lista productos
  - `POST /products` → crea producto `{ name, price }`

### Ejecutar
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```
API en: `http://127.0.0.1:8000/products`

## Frontend
- **Stack:** React + Vite + TailwindCSS + Axios

### Ejecutar
```bash
cd frontend
npm install
npm run dev
```
App en: `http://127.0.0.1:5173/`

> Asegúrate de que el backend esté corriendo en `http://127.0.0.1:8000`.

## Estructura
```
prueba-tecnica/
  backend/
    main.py
    requirements.txt
  frontend/
    package.json
    vite.config.js
    tailwind.config.js
    postcss.config.cjs
    index.html
    src/
      main.jsx
      App.jsx
      index.css
```
