// *** code.js ***
// Ici c'est la place du code Javascript!

// @view()
// Cette fonction permet de charger du HTML depuis l'URL passée en paramètre 's'
// et de l'insérer dans l'élément 'view_div' (en tant que texte HTML).
// => cf. menu de la page 'index.html'
function view(s)
{
    // Async. HTTP depuis le Javascript...
    var httpReq = new XMLHttpRequest();

    httpReq.onreadystatechange = function()
    {
        if (httpReq.readyState == 4 && httpReq.status == 200)
        {
            view_div.innerHTML = httpReq.responseText;
        }
        else
        {
            view_div.innerHTML = "..."
        }
    };

    httpReq.open("GET", s, true);
    httpReq.send(null);
}