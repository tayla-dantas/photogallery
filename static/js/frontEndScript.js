
function fileUpload(){ 
    var fileInput = $("#file")
    var button =$("#uploadFile")
    fileInput.onchange = () => {
        alert("uhuu");
    }
};

window.onload = fileUpload;