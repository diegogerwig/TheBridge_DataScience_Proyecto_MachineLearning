<!-- Markdown con HTML para un encabezado fijo -->
<html>
<head>
<style>
  body {
    margin-top: 100px;
  }
  .fixed-header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background-color: #333;
    color: white;
    padding: 15px 5px;
    z-index: 1000;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-direction: column; 
  }
  .logos {
    display: flex;
    justify-content: space-between;
    width: 100%;
    max-width: 1000px; 
    padding: 0 50px; 
    box-sizing: border-box; 
  }
  .logo-left {
    height: 60px; 
  }
  .logo-right {
    height: 40px; 
  }
  .header-content {
    text-align: center;
    margin-top: 10px; 
  }
</style>
</head>
<body>

<div class="fixed-header">
  <div class="logos">
    <img src="../img/traffic_crash.png" alt="Imagen Izquierda" class="logo-left">
    <img src="../img/logo_theBridge.svg" alt="Imagen Derecha" class="logo-right">
  </div>
  <div class="header-content">
    <h1>TRAFFIC ACCIDENTS ANALISYS</h1>
  </div>
</div>

#
#
#

# Título 1

Contenido debajo del encabezado fijo.

## Título 2

Más contenido.

</body>
</html>