(function(win,doc){
  'use strict';

  //Verifica se o usuário realmente quer deletar o dado
  if(doc.querySelector('.bdel')){
    let bdel = doc.querySelectorAll('.bdel');
    for(let i=0; i < bdel.length; i++){
        bdel[i].addEventListener('click', function(event){
          if(confirm('Confirmar a exclusão desse registro?')) {
            sessionStorage.setItem('del', "1");
            return true;
          }else{
            event.preventDefault();
          }
        });
    }
  }
})(window,document);

notificar();
sessionStorage.clear();

// Notificação
let closea = document.querySelector('.nclose');

closea.addEventListener('click', (event) => {
  event.preventDefault();
  close();
})

function close() {
  let notification = document.getElementById('notificacao');
  notification.style.right = "-25%";
  notification.style.visibility = "hidden";
};

function notificar() {
  let notification = document.getElementById('notificacao');

  function bye() {
    setTimeout(function(){
      close();
    },6000);
  };

  let notifi = document.querySelector('.notifi');

  if (!(sessionStorage.getItem('del') === null)) {
    notification.style.visibility = "visible";
    notifi.innerHTML = `Cliente deletado<br>com sucesso!`;
    notification.style.backgroundColor = "#e84c62";
    bye();
  };

  if (!(sessionStorage.getItem('edit') === null)) {
    notification.style.visibility = "visible";
    notifi.innerHTML = `Cliente editado<br>com sucesso!`;
    notification.style.backgroundColor = "#dab33e";
    bye();
  };

  if (!(sessionStorage.getItem('add') === null)) {
    notification.style.visibility = "visible";
    notifi.innerHTML = `Cliente adicionado<br>com sucesso!`;
    notification.style.backgroundColor = "#287cfb";
    bye();
  };

};