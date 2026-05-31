# CHANGELOG

## Evolución de la Propuesta Inicial hacia una Arquitectura MLOps

Este documento resume los principales cambios realizados sobre la propuesta inicial presentada en la primera parte del taller. El objetivo de esta evolución fue transformar un pipeline tradicional de Machine Learning en una arquitectura MLOps completa capaz de soportar desarrollo, despliegue, monitoreo y mantenimiento continuo de modelos en producción.

---

# Resumen General

La propuesta inicial estaba enfocada principalmente en las etapas clásicas de Machine Learning:

- Recolección de datos.
- Limpieza de datos.
- Ingeniería de características.
- Entrenamiento.
- Evaluación.
- Despliegue.
- Monitoreo básico.

La nueva propuesta incorpora prácticas modernas de MLOps para garantizar:

- Reproducibilidad.
- Trazabilidad.
- Automatización.
- Calidad del software.
- Monitoreo continuo.
- Escalabilidad futura.

---

# 1. Gestión de Datos

## Propuesta Inicial

La propuesta original contemplaba la adquisición, limpieza y preparación de datos como parte del flujo de entrenamiento.

## Nueva Propuesta

Se incorporan tres componentes adicionales:

### PostgreSQL

Permite centralizar y almacenar la información clínica de manera estructurada.

### Great Expectations

Introduce validaciones automáticas de calidad de datos antes de iniciar cualquier proceso de entrenamiento o inferencia.

### DVC

Permite versionar datasets y mantener trazabilidad completa sobre los datos utilizados durante cada entrenamiento.

## Beneficio

Se mejora significativamente la reproducibilidad y confiabilidad de los datos utilizados por el sistema.

---

# 2. Manejo del Desbalance de Clases

## Propuesta Inicial

La propuesta original no contemplaba explícitamente el problema del desbalance entre enfermedades comunes y enfermedades huérfanas.

## Nueva Propuesta

Se incorpora la librería imbalanced-learn junto con técnicas como:

- Oversampling.
- Undersampling.
- SMOTE.

## Beneficio

Se reduce el sesgo hacia enfermedades frecuentes y se mejora la capacidad del modelo para identificar enfermedades poco comunes.

---

# 3. Entrenamiento y Gestión de Modelos

## Propuesta Inicial

La propuesta original contemplaba entrenamiento y evaluación de modelos sin mecanismos formales de trazabilidad de experimentos.

## Nueva Propuesta

Se incorporan múltiples modelos candidatos:

- Logistic Regression.
- Random Forest.
- XGBoost.
- CatBoost.

Adicionalmente se integra MLflow para registrar:

- Hiperparámetros.
- Métricas.
- Artefactos.
- Versiones de modelos.

## Beneficio

Permite comparar experimentos de forma objetiva y reproducir resultados históricos.

---

# 4. Calidad del Software

## Propuesta Inicial

No existían mecanismos explícitos de validación automática del código.

## Nueva Propuesta

Se incorporan pruebas unitarias utilizando Pytest.

Estas pruebas son ejecutadas automáticamente durante el proceso de integración continua.

## Beneficio

Reduce la probabilidad de introducir errores en producción.

---

# 5. Integración Continua y Automatización

## Propuesta Inicial

Los procesos de validación y despliegue eran principalmente manuales.

## Nueva Propuesta

Se implementa un pipeline CI/CD utilizando GitHub Actions.

### Eventos Automatizados

#### Pull Request

- Comentario inicial.
- Ejecución de pruebas.
- Comentario final.

#### Push a la Rama Principal

- Ejecución de pruebas.
- Construcción de imagen Docker.
- Publicación automática en GitHub Container Registry (GHCR).

## Beneficio

Se mejora la calidad del software y se reduce la intervención manual durante el ciclo de desarrollo.

---

# 6. Despliegue

## Propuesta Inicial

La propuesta contemplaba un despliegue genérico del modelo.

## Nueva Propuesta

Se incorpora:

### Docker

Permite empaquetar la aplicación y garantizar reproducibilidad entre ambientes.

### FastAPI

Expone el modelo mediante una API REST para consumo remoto.

### GitHub Container Registry (GHCR)

Permite almacenar y distribuir imágenes Docker versionadas.

## Beneficio

Facilita la distribución, despliegue y mantenimiento de la solución.

---

# 7. Soporte para Ejecución Local y Remota

## Propuesta Inicial

No se definían claramente los escenarios de despliegue.

## Nueva Propuesta

Se contemplan dos modalidades de operación:

### Ejecución Local

El médico ejecuta la solución directamente mediante Docker.

### Ejecución Remota

El médico consume el modelo mediante una API desplegada en un servidor o proveedor cloud.

## Beneficio

La solución se adapta a diferentes contextos operativos y restricciones de infraestructura.

---

# 8. Monitoreo y Operación Continua

## Propuesta Inicial

Existía un monitoreo general sin mecanismos específicos de detección de degradación.

## Nueva Propuesta

Se incorpora Evidently para monitorear:

### Data Drift

Cambios en la distribución de los datos de entrada.

### Concept Drift

Cambios en la relación entre síntomas y enfermedades.

También se define una estrategia de reentrenamiento basada en las alertas generadas por el monitoreo.

## Beneficio

Permite mantener el desempeño del modelo a lo largo del tiempo.

---

# 9. Escalabilidad Futura

## Propuesta Inicial

No se contemplaban mecanismos de escalabilidad.

## Nueva Propuesta

Se identifican tecnologías que podrían incorporarse en escenarios de mayor complejidad:

- Apache Airflow.
- Apache Spark.
- PySpark.
- Prometheus.
- Grafana.

## Beneficio

La arquitectura queda preparada para evolucionar hacia escenarios con mayor volumen de datos y mayores requerimientos operativos.

---

# Resultado Final

La propuesta evolucionó desde un pipeline tradicional de Machine Learning hacia una arquitectura MLOps completa que incorpora:

- Gestión de datos.
- Control de calidad.
- Versionado de datasets.
- Seguimiento de experimentos.
- Automatización CI/CD.
- Pruebas unitarias.
- Contenerización.
- Despliegue reproducible.
- Monitoreo continuo.
- Estrategias de reentrenamiento.

Estos cambios permiten construir una solución más robusta, mantenible y preparada para operar en entornos clínicos reales.