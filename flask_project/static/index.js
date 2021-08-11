document.getElementById('fucking-form').onsubmit = (e) => {
    e.preventDefault();

    const formData  = new FormData();
    const fileInput1 = document.getElementById('cute-image-input');
    const fileInput2 = document.getElementById('cute-music-input');
    formData.append('initial_image', fileInput1.files[0]);
    formData.append('initial_music', fileInput2.files[0]);

    fetch('/add', {
        method: 'POST',
        body: formData
    })
    .then(r => r.json())
    .then(data => {
        console.log(data);
        // const imageElement = document.getElementById('result-image')
        // imageElement.src = data['image_url']
        document.getElementById('image-container_final').innerHTML = `
        <img src="${ data['image_final_url'] }" style="width: 600px;">
        <img src="${ data['music_image_url'] }" style="width: 600px;">
        `;

    })
}