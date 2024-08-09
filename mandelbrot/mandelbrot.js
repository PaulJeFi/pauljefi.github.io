var canvas = document.querySelector('#my-canvas');
var context = canvas.getContext('2d');

function range(arg, arg2=0, arg3=0) {
    // La fonction range de Python !!!
    let list = [];
    if (arg2 != 0) {
        if (arg3 == 0) {
            let a = 0;
            while (a != arg2) {
                list.push(a);
                a += 1;
            }
        } else {
            let a = arg;
            let b = arg2;
            while (a != b) {
                list.push(a);
                a += 1;
            }
        }
    } else {
        let a = 0;
        while (a != arg) {
            list.push(a);
            a += 1;
        }
    }
    return list;
}

function linspace(x_min, x_max, number) {
    // La fonction linspace de Numpy !!!
    let array = [];
    let step = (x_max-x_min)/number;
    let here = x_min;
    while (array.length < number) {
        array.push(here);
        here += step;
    }
    return array;
}

function changesize(element) {
    element.style.fontSize = "20px";
}
function resertsize(element) {
    element.style.fontSize = "10px";
}

function mouseenter(element) {
    element.style.backgroundColor = "red";
    element.style.color = "white";
    element.style.height = "30px";
    element.style.width = "70px";
}
function mouseleave(element) {
    element.style.backgroundColor = "white";
    element.style.color = "black";
    element.style.height = "20px";
    element.style.width = "50px";
}

function drawPixel(x, y, color) {
    // Placer un pixel de couleur sur le canvas
    var roundedX = Math.round(x);
    var roundedY = Math.round(y);

    context.beginPath();
    context.fillStyle = color || '#000';
    context.fillRect(roundedX, roundedY, 1, 1);
    context.fill();
}

function cardioide(x, y) {
    // Determine si le point appartient a la cardioide
    // https://fr.wikipedia.org/wiki/Ensemble_de_Mandelbrot
    p = ( (x-1/4)**2 + y**2 ) ** 0.5;
    return x < p - 2*(p**2) + 1/4;
}

function bourgeon_principal(x, y) {
    // Determine si le point appartient au bourgeon pincipal
    // https://fr.wikipedia.org/wiki/Ensemble_de_Mandelbrot
    return (x+1)**2 + y**2 < 1/16;
}

function mandelbrot(iter) {
    // Trace l'ensemble de Mandelbrot

    let iteration = document.get_iter.iter.value;

    // palette de couleurs
    let palette = [];
    let rgb = [123, 12, 255]
    for (let i of range(iteration)) {
        palette.push([rgb[0]*i/iteration, rgb[1]*i/iteration, rgb[2]*i/iteration]);
    }
    for (let i of range(iteration)) {
        palette.push([rgb[0]*i/iteration, rgb[1]*i/iteration, rgb[2]*i/iteration]);
    }
    for (let i of range(iteration)) {
        palette.push([rgb[0]*i/iteration, rgb[1]*i/iteration, rgb[2]*i/iteration]);
    }

    //palette = palette.reverse()

    let height = canvas.height;
    let width = canvas.width;

    let X = linspace(-2, 0.5, width);
    let Y = linspace(-2.5/2, 2.5/2, height);

    let y_index = 0;
    let x_index = 0;

    for (let y of Y.slice(0, Math.floor(height/2))) {
        x_index = 0;
        for (let x of X) {
            if (cardioide(x, y) || bourgeon_principal(x, y) && false) {
                drawPixel(x_index, y_index, "rgb(0, 0, 0)");
                drawPixel(x_index, height-1-y_index, "rgb(0, 0, 0)");
            } else {

                let z = [0, 0];
                let c = [x, y];

                let i = 0
                for (let a of range(iteration)) {

                    z = [(z[0]**2)-(z[1]**2)+c[0], 2*z[0]*z[1]+c[1]]
                    i++

                    if (((z[0]**2 + z[1]**2) ** 0.5) > 2) {
                        break;
                    }
                }

                if (i == iteration) {
                    drawPixel(x_index, y_index, "rgb(0, 0, 0)");
                    drawPixel(x_index, height-1-y_index, "rgb(0, 0, 0)");
                } else {
                    let r = palette[i][0];
                    let g = palette[i][1];
                    let b = palette[i][2];
                    r = r.toString();
                    g = g.toString();
                    b = b.toString();
                    let color = "rgb("+r+","+g+","+b+")";
                    drawPixel(x_index, y_index, color);
                    drawPixel(x_index, height-1-y_index, color);
                }
            }

            x_index++;
        }
        y_index++;
    }
}