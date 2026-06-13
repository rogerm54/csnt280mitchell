function removeChildren(elem) {
   while (elem.childNodes.length > 0) {
      elem.removeChild(elem.childNodes[0]);
   }
}
function toggle_answer(answer_div_id,button_id) {
  var answer_div = document.getElementById(answer_div_id);
  var button = document.getElementById(button_id);
  console.log('button.childNodes',button.childNodes);
  var label = button.innerHTML.trim();
  console.log('label',label);
  if (label == "Show") {
    answer_div.style.display = "block";
    removeChildren(button);
    var label2 = document.createTextNode("Hide");
    button.appendChild(label2);
  }
  else {
    answer_div.style.display = "none";
    var label2 = document.createTextNode("Show");
    removeChildren(button);
    button.appendChild(label2);
  }
}
