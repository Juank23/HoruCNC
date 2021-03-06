document.addEventListener('click', function (event) {

    // If the clicked element doesn't have the right selector, bail
    switch(event.target.id){
        case "probe-up":
            fetch("/machine/pendant/Z/1/100", {method: "POST"})
            break;
        case "probe-down":
            fetch("/machine/pendant/Z/-0.5/100", {method: "POST"})
            break;
        case "probe-start":
            fetch("/machine/probe/-20/10", {method: "POST"})
            break;
        case "carve-start":
            fetch("/machine/carve/start", {method: "POST"})
            break;
    }

}, false);

