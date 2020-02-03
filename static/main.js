function submitForm() {
    console.log("submit event");

    var fd = new FormData(document.getElementById("fileinfo"));
    //document.getElementById("makegood").hidden = false;
    let elem = document.getElementById("makegood")
    console.log("wtf");
    
		elem.removeAttribute('hidden');
		document.getElementById("this2").setAttribute('hidden', 'true');

    $.ajax({
      url: "calculate/",
      
      type: "POST",
      data: fd,
      processData: false,  // tell jQuery not to process the data
      contentType: false,
      success: function(data){
        //$(this).addClass("done");
        elem.setAttribute('hidden', 'true');
        
        document.getElementById("this2").innerHTML =  "<strong>" + String(parseFloat(data["rsvp"]).toPrecision(3)) + "</strong>";
        document.getElementById("this2").removeAttribute('hidden');
      }   // tell jQuery not to set contentType
      
    });
    //document.getElementById("makegood").style.visibility = 'hidden';
    
    console.log("jesusmoses")
    return false;
}
