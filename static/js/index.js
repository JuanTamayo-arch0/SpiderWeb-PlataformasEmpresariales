
/*import b1 from '../assets/img/banner1.png'
import b2 from '../assets/img/banner2.png'
import b3 from '../assets/img/banner3.png'*/


/* Dark Mode */

const button = document.getElementById('darkModeToggle');
    const div1 = document.getElementById('c1');
    const div2 = document.getElementById('movies');
    const div3 = document.getElementById('n1');
    const div4 = document.getElementById('f1');
    const div5 = document.getElementById('c3');
    const div6 = document.getElementById('ib');
    const div7 = document.getElementById('ib2');
    const div8 = document.getElementById('ib3');
    const div9 = document.getElementById('r');
    const div10 = document.getElementById('r2');

    button.addEventListener('click', () => {             
      document.body.classList.toggle('dark-mode'); 
      div1.classList.toggle('dark-mode'); 
      div2.classList.toggle('dark-mode'); 
      div3.classList.toggle('dark-mode'); 
      div4.classList.toggle('dark-mode'); 
      div5.classList.toggle('dark-mode'); 
      div6.classList.toggle('dark-mode'); 
      div7.classList.toggle('dark-mode'); 
      div8.classList.toggle('dark-mode'); 
      div9.classList.toggle('dark-mode');
      div10.classList.toggle('dark-mode');
    });   
    
    
/* user custom */

/* CARRUSEL */

document.querySelector('.menu-toggle').addEventListener('click', function() {
  document.querySelector('.links').classList.toggle('active');
});



class Carousel {
  constructor(el) {
    this.el = el;
    this.carouselOptions = ['previous', 'add', 'play', 'next'];
    this.carouselData = [
      {
        'id': '1',
        'src': b1,
      },
      {
        'id': '2',
        'src': b2,
      },
      {
        'id': '3',
        'src': b3,
      },
      
    ];
    this.carouselInView = [1, 2, 3];
    this.carouselContainer;
    this.carouselPlayState;
  }

  mounted() {
    this.setupCarousel();
  }

  // Build carousel html
  setupCarousel() {
    const container = document.createElement('div');
    const controls = document.createElement('div');

    // Add container for carousel items and controls
    this.el.append(container, controls);
    container.className = 'carousel-container';
    controls.className = 'carousel-controls';

    // Take dataset array and append items to container
    this.carouselData.forEach((item, index) => {
      const carouselItem = item.src ? document.createElement('img') : document.createElement('div');

      container.append(carouselItem);
      
      // Add item attributes
      carouselItem.className = `carousel-item carousel-item-${index + 1}`;
      carouselItem.src = item.src;
      carouselItem.setAttribute('loading', 'lazy');
      // Used to keep track of carousel items, infinite items possible in carousel however min 5 items required
      carouselItem.setAttribute('data-index', `${index + 1}`);
    });

    this.play();

    // Set container property
    this.carouselContainer = container;
  }

  setControls(controls) {
 
    controls.forEach(control => {
      control.onclick = (event) => {
        event.preventDefault();

        // Manage control actions, update our carousel data first then with a callback update our DOM
        this.controlManager(control.dataset.name);
      };
    });
    this.play();
  }

  controlManager(control) {

    this.control = 'play';
    
    if (control === 'previous') return this.previous();
    if (control === 'next') return this.next();
    if (control === 'add') return this.add();
    if (control === 'play') return this.play();

    return;
  }


  next() {
    // Update order of items in data array to be shown in carousel
    this.carouselData.push(this.carouselData.shift());

    // Take the last item and add it to the beginning of the array so that the next item is front and center
    this.carouselInView.unshift(this.carouselInView.pop());

    // Update the css class for each carousel item in view
    this.carouselInView.forEach((item, index) => {
      this.carouselContainer.children[index].className = `carousel-item carousel-item-${item}`;
    });

    // Using the first 5 items in data array update content of carousel items in view
    this.carouselData.slice(0, 5).forEach((data, index) => {
      document.querySelector(`.carousel-item-${index + 1}`).src = data.src;
    });
  }

  play() {
    const playBtn = document.querySelector('.carousel-control-play');
    const startPlaying = () => this.next();

      this.carouselPlayState = setInterval(startPlaying, 1500);
 
  }

}

// Refers to the carousel root element you want to target, use specific class selectors if using multiple carousels
const el = document.querySelector('.carousel');
// Create a new carousel object
const exampleCarousel = new Carousel(el);
// Setup carousel and methods
exampleCarousel.mounted();
