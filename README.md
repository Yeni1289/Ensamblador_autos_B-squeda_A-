# Heurística Admisible - Selección Óptima de Ruedas

Aplicación interactiva en Streamlit que usa el algoritmo **A*** para encontrar la asignación óptima de proveedores de ruedas por tipo, respetando la restricción de usar una empresa distinta para cada tipo de rueda.

## 📋 Descripción del problema

Una empresa de fabricación de vehículos necesita comprar 4 tipos de ruedas (T, H, V, W) de 4 proveedores distintos. Cada proveedor tiene precios diferentes por tipo de rueda.

**Restricción**: Usar exactamente una empresa distinta para cada tipo de rueda.

**Objetivo**: Minimizar el costo total de compra.

## 🔍 Algoritmo: A* con Heurística Admisible

La aplicación implementa:

- **Búsqueda A***: Algoritmo óptimo que expande nodos con menor costo estimado f(n) = g(n) + h(n)
- **Heurística Admisible**: h(n) = suma de los precios mínimos disponibles para ruedas pendientes
  - Nunca sobreestima el costo real
  - Garantiza optimalidad

## 🚀 Estructura del Proyecto

```
empresa-de-veiculos/
├── app.py                      # Interfaz principal (Python)
├── requirements.txt            # Dependencias
├── .gitignore
├── .streamlit/
│   └── config.toml             # Configuración de Streamlit
│
├── src/
│   ├── __init__.py
│   └── solver.py               # Algoritmo A* (Python)
│
└── assets/
    ├── components/
    │   └── hero.html           # Cabecera (HTML)
    │
    └── styles/
        └── main.css            # Diseño (CSS)
```

## 🛠️ Instalación Local

### Requisitos
- Python 3.8+
- pip

### Pasos

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/Yeni1289/Ensamblador_autos_B-squeda_A-.git
   cd empresa-de-veiculos
   ```

2. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la app**
   ```bash
   streamlit run app.py
   ```

4. **Abrir en el navegador**
   ```
   http://localhost:8501
   ```

## 🌐 Despliegue en Streamlit Cloud

1. Sube el repositorio a GitHub (ya hecho ✓)

2. Ve a [Streamlit Cloud](https://share.streamlit.io/)

3. Haz clic en "New app"

4. Selecciona:
   - Repository: `Yeni1289/Ensamblador_autos_B-squeda_A-`
   - Branch: `main`
   - File path: `app.py`

5. Haz clic en "Deploy"

La app estará disponible en: `https://share.streamlit.io/Yeni1289/Ensamblador_autos_B-squeda_A-/main/app.py`

## 📊 Ejemplo de Uso

Precios por defecto:

| Empresa | Tipo T | Tipo H | Tipo V | Tipo W |
|---------|--------|--------|--------|--------|
| Empresa 1 | $20 | $30 | $20 | $40 |
| Empresa 2 | $30 | $50 | $40 | $50 |
| Empresa 3 | $60 | $55 | $50 | $60 |
| Empresa 4 | $100 | $80 | $60 | $70 |

**Solución óptima**:
- Tipo T → Empresa 2: $30
- Tipo H → Empresa 3: $55
- Tipo V → Empresa 1: $20
- Tipo W → Empresa 4: $70
- **Total: $175** ✓

## 🎨 Características

- ✅ Interfaz interactiva: edita precios en tiempo real
- ✅ Resultado óptimo global con A*
- ✅ Validación automática: A* vs fuerza bruta
- ✅ Diseño responsivo con tema azul
- ✅ Separación de lenguajes: Python, HTML, CSS

## 📝 Lenguajes Utilizados

- **Python**: Lógica y algoritmo (app.py, src/solver.py)
- **HTML**: Componentes (assets/components/hero.html)
- **CSS**: Diseño visual (assets/styles/main.css)

## 📚 Referencias Teóricas

### Función g(n)
Costo acumulado desde el inicio hasta el nodo actual.

### Función h(n)
Estimación del costo restante (heurística admisible).

### Función f(n)
f(n) = g(n) + h(n) - valor usado por A* para ordenar la cola de prioridad.

## 👥 Autor

Creado como proyecto educativo para demostrar algoritmos de búsqueda con heurística admisible.

## 📄 Licencia

MIT License - libre de usar y modificar.
