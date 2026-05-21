# 🚀 Guía de Despliegue en Streamlit Cloud

## Paso 1: Verificar repositorio en GitHub

✅ Tu repositorio está en: https://github.com/Yeni1289/Ensamblador_autos_B-squeda_A-

Verifica que todos los archivos estén presentes:
- ✓ app.py
- ✓ requirements.txt
- ✓ src/solver.py
- ✓ assets/styles/main.css
- ✓ assets/components/hero.html
- ✓ .streamlit/config.toml
- ✓ README.md

## Paso 2: Ir a Streamlit Cloud

1. Ve a: https://share.streamlit.io/
2. Haz login con tu cuenta de GitHub (si no tienes, crea una)

## Paso 3: Crear nueva app

1. Haz clic en el botón **"Create app"** (esquina superior derecha)
2. Se abrirá un modal con los siguientes campos:

   **Repository**: 
   ```
   Yeni1289/Ensamblador_autos_B-squeda_A-
   ```

   **Branch**: 
   ```
   main
   ```

   **File path**: 
   ```
   app.py
   ```

3. Haz clic en **"Deploy"**

## Paso 4: Esperar despliegue

- El proceso toma 2-5 minutos
- Verás un indicador de progreso
- Tu app estará disponible en una URL similar a:
  ```
  https://share.streamlit.io/yeni1289/ensamblador_autos_b-squeda_a-/main/app.py
  ```

## Paso 5: Compartir la app

Una vez desplegada, puedes:
- Copiar la URL y compartirla
- Incrustarlo en un sitio web
- Acceder desde cualquier dispositivo

## 🔧 Solucionar problemas

### Error: "app.py not found"
- Asegúrate de que el archivo `app.py` está en la raíz del repositorio
- Verifica el nombre exacto (case-sensitive)

### Error: "ModuleNotFoundError"
- Asegúrate de que `requirements.txt` contiene todas las dependencias
- Actualmente contiene:
  ```
  streamlit
  pandas
  ```

### Error: Archivo CSS no se carga
- El archivo debe estar en: `assets/styles/main.css`
- Verifica que la ruta en `app.py` sea: `Path("assets/styles/main.css")`

### Error: HTML no se renderiza
- El archivo debe estar en: `assets/components/hero.html`
- Verifica que la ruta sea: `Path(f"assets/components/{filename}")`

## 📊 Monitoreo

Una vez desplegada:
- Accede a tu dashboard en: https://share.streamlit.io/
- Verás logs, estadísticas de uso, y podrás ver errores en tiempo real
- Puedes revisar el estado con el botón "Manage app"

## 🔄 Actualizar la app

Para actualizar el código desplegado:

1. Haz cambios en tu repositorio local
2. Haz commit y push a GitHub:
   ```bash
   git add .
   git commit -m "Descripción del cambio"
   git push origin main
   ```

3. Streamlit Cloud detectará automáticamente los cambios
4. La app se redesplegará automáticamente (toma 1-2 minutos)

## 💡 Tips

- Usa secrets en Streamlit: `.streamlit/secrets.toml` para datos sensibles
- El archivo de configuración está en `.streamlit/config.toml`
- Los logs se pueden ver en el dashboard
- Puedes cambiar el nombre de la app en "Settings"

## ✅ Verificación Final

Cuando la app esté desplegada:
1. ✓ Carga la página en navegador
2. ✓ Edita precios en la tabla
3. ✓ Verifica que calcula el costo óptimo
4. ✓ Confirma que muestra las 3 métricas
5. ✓ Revisa que la tabla de resultados aparece

¡Listo! Tu app está desplegada. 🎉
