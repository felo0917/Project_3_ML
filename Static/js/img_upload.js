// const inputFile = document.getElementById('inputFile');
// const prevContainer = document.getElementById('imagePreview');
// const prevImg = prevContainer.querySelector('.img_prev_img');
// const prevDeftext = prevContainer.querySelector('.img_prev_text');


// inputFile.addEventListener('change', function() {
//     const file = this.files[0];

//     console.log(file)

//     if (file) {
//         const reader = new FileReader();

//         prevDeftext.style.display = 'none';
//         prevImg.style.display = 'block';

//         reader.addEventListener('load', function() {
           
//             prevImg.setAttribute('src', this.result);
//         });

//         reader.readAsDataURL(file);
//     }
// });