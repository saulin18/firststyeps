python

data = [
    ["Elemento 1", "Información 1"],
    ["Elemento 2", "Información 2"],
    ["Elemento 3", "Información 3"],
    ["Elemento 4", "Información 4"],
    ["Elemento 5", "Información 5"],
    # ... Puedes agregar más filas si es necesario
]

# Función para imprimir la tabla con desplazamiento vertical
def print_table_with_scroll(data, max_rows=5):
    headers = ["Elemento", "Información"]
    row_format = "{:<15}" * (len(headers) + 1)
    num_rows = len(data)

    if num_rows > max_rows:
        print(row_format.format(*headers))
        print("-" * 30)
        for row in data[:max_rows]:
            print(row_format.format("", *row))
        print("...")  # Indicador de que hay más filas
    else:
        print(row_format.format(*headers))
        print("-" * 30)
        for row in data:
            print(row_format.format("", *row))

# Llamamos a la función para imprimir la tabla con desplazamiento vertical
print_table_with_scroll(data)




const myCarouselElement = document.querySelector('#myCarousel')


const carousel = new bootstrap.Carousel(myCarouselElement, {
  interval: 500,
  touch: true
})

const myCarousel = document.getElementById('myCarousel')

myCarousel.addEventListener('slide.bs.carousel', event => {
  
})



<button class="btn btn-primary" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasWithBothOptions" aria-controls="offcanvasWithBothOptions">Enable both scrolling & backdrop</button>

<div class="offcanvas offcanvas-start" data-bs-scroll="true" tabindex="-1" id="offcanvasWithBothOptions" aria-labelledby="offcanvasWithBothOptionsLabel">
  <div class="offcanvas-header">
    <h5 class="offcanvas-title" id="offcanvasWithBothOptionsLabel">Backdrop with scrolling</h5>
    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
  </div>
  <div class="offcanvas-body">
    <p>Try scrolling the rest of the page to see this option in action.</p>
  </div>
</div>

<nav class="nav">
    
    <input type="checkbox" id="nav_checkbox" class="nav_checkbox" />
    
    <label for="nav_checkbox" class="nav_toggle">
      
      <svg class="menu" viewBox="0 0 448 512" width="100" title="bars">
        <path d="M16 132h416c8.837 0 16-7.163 16-16V76c0-8.837-7.163-16-16-16H16C7.163 60 0 67.163 0 76v40c0 8.837 7.163 16 16 16zm0 160h416c8.837 0 16-7.163 16-16v-40c0-8.837-7.163-16-16-16H16c-8.837 0-16 7.163-16 16v40c0 8.837 7.163 16 16 16zm0 160h416c8.837 0 16-7.163 16-16v-40c0-8.837-7.163-16-16-16H16c-8.837 0-16 7.163-16 16v40c0 8.837 7.163 16 16 16z" />
      </svg>
      <svg class="close" viewBox="0 0 384 512" width="100" title="times">
        <path d="M242.72 256l100.07-100.07c12.28-12.28 12.28-32.19 0-44.48l-22.24-22.24c-12.28-12.28-32.19-12.28-44.48 0L176 189.28 75.93 89.21c-12.28-12.28-32.19-12.28-44.48 0L9.21 111.45c-12.28 12.28-12.28 32.19 0 44.48L109.28 256 9.21 356.07c-12.28 12.28-12.28 32.19 0 44.48l22.24 22.24c12.28 12.28 32.2 12.28 44.48 0L176 322.72l100.07 100.07c12.28 12.28 32.2 12.28 44.48 0l22.24-22.24c12.28-12.28 12.28-32.19 0-44.48L242.72 256z" />
      </svg>
      
    </label> 
   
    <ul class="nav_menu">
      
      <li> <img src="minsi.png" alt="EBENEZER LOGO" id="navL"></li>
      <li><a href="#">Contacto</a> <img src="https://img.icons8.com/?size=64&id=nDoZO3ymyexY&format=png&color=1A6DFF,C822FF" alt="Mensajes" class="loguitos">   </li>
      <li><a href="#">Aportaciones</a> <img src="https://img.icons8.com/?size=64&id=50919&format=png&color=1A6DFF,C822FF" alt="Paypal"  class="loguitos"></li>
      <li><a href="#">Instagram</a> <img src="https://img.icons8.com/?size=64&id=43625&format=png&color=1A6DFF,C822FF" alt="Instagram"  class="loguitos"></li>
      <li><a href="#">Telegram</a> <img src="https://img.icons8.com/?size=64&id=114954&format=png&color=1A6DFF,C822FF" alt="Telegram"  class="loguitos"></li>
      
    </ul>
    
  </nav>

  <details>
    <summary>NUESTRAS REDES SOCIALES.
    </summary>
    <ul><br>
      <br><li><br><a href="https://www.facebook.com/iglesiaeltabernaculoebenezerhg/" target="_blank">NUESTRA PÁGINA DE FACEBOOK.</a> <br> <img src="https://img.icons8.com/?size=64&id=123743&format=png&color=1A6DFF,C822FF"   alt="FACEBOOK"    class="loguitos"></li><br>
      <li><a href="https://www.youtube.com/c/IglesiadeCristoElTabern%C3%A1culoEbenezer" target="_blank">NUESTRO CANAL DE YOUTUBE.</a> <br><img src="https://img.icons8.com/?size=64&id=44112&format=png&color=1A6DFF,C822FF"  alt="YOUTUBE"    class="loguitos"></li><br>
      <li><a href="https://www.youtube.com/@JuanyLisney" target="_blank">EL CANAL DE YOUTUBE DE NUESTROS PADRES. </a> <br> <img src="https://img.icons8.com/?size=64&id=44112&format=png&color=1A6DFF,C822FF"   alt="YOUTUBE"     class="loguitos"> </li><br>
        <li><a href="https://www.facebook.com/juanylisney/
            " target="_blank">LA PÁGINA DE FACEBOOK DE NUESTROS PADRES. </a> <br><img src="https://img.icons8.com/?size=64&id=123743&format=png&color=1A6DFF,C822FF"  alt="FACEBOOK"  class="loguitos"></li>
    </ul>
  </details>

  <a class="nav-link dropdown-toggle" href="#" role="button"  data-bs-toggle="tooltip" data-bs-title="Ayudanos compartiendo para alcanzar a más personas" aria-expanded="false">
                    Redes sociales
                  </a>



                  <div id="carouselExampleControlsNoTouching" class="carousel slide" data-bs-touch="true">
            <div class="carousel-inner">
              <div class="carousel-item active">
                <img src="inicio primera.png" class="d-block w-100" alt="...">
              </div>
              <div class="carousel-item">
                <img src="inicio 2da.png" class="d-block w-100" alt="...">
              </div>
              <div class="carousel-item">
                <img src="inicio 3ra.png" class="d-block w-100" alt="...">
              </div>
              <div class="carousel-item">
                <img src="fondo inicio.jpg" class="d-block w-100" alt="...">
              </div>
              <div class="carousel-item">
                <img src="braña sin techo.jpg" class="d-block w-100" alt="...">
              </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControlsNoTouching" data-bs-slide="prev">
              <span class="carousel-control-prev-icon" aria-hidden="true"></span>
              <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControlsNoTouching" data-bs-slide="next">
              <span class="carousel-control-next-icon" aria-hidden="true"></span>
              <span class="visually-hidden">Next</span>
            </button>
          </div>