function previewMedia(input) {
    var preview = document.getElementById('preview');
    var imagePreview = document.getElementById('imagePreview');

    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function(e) {
            preview.src = e.target.result;
            imagePreview.style.display = 'block';
        }

        reader.readAsDataURL(input.files[0]);
    }
}