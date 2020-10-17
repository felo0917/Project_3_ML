

// create variables to capture image preview, file tht was uploaded and the name on the image file

const inputFile = document.getElementById('inputFile');
const prevContainer = document.getElementById('imagePreview');
const prevImg = prevContainer.querySelector('.img_prev_img');
const prevDeftext = prevContainer.querySelector('.img_prev_text');



// use a function to show the image when the user selects the file from their local machine 

inputFile.addEventListener('change', function() {

    // file is the file input
    const file = this.files[0];

    // console.log(file)

    // if there's a file that is selected, read the preview text and show image in the img display box

    if (file) {
        const reader = new FileReader();

        prevDeftext.style.display = 'none';

        prevImg.style.display = 'block';

        reader.addEventListener('load', function() {
        
            // "this" is reference to the result URL that FileReader is capturing
            prevImg.setAttribute('src', this.result);
        });

        // read the file once loaded and show
        reader.readAsDataURL(file);
    
    } else {
    
    // else show nothing on the image, text 

        prevDeftext.style.display = null;
        prevImg.style.display = null;
        prevImg.setAttribute('src','')
    }

});

