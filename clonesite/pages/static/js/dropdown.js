var bigmama = document.getElementsByTagName('html')[0];
    var accesMenu = document.querySelector('[data-name="LARGE_UP_MAIN_NAV_TRIGGER"]')
    var removeMenu = document.querySelector('[data-name="MAIN_NAV_TRIGGER_CONTAINER"]')
    var blanketObject = document.getElementsByName('BLANKET')[0];
    var dropDownMenu = document.getElementsByClassName("js-main-nav-dropdown")[0];
    var listys = document.querySelectorAll('a[data-name="NAV_SUBSECTION_PARENT"]');
    for (var i = 0; i < listys.length; i++) {
      listys[i].addEventListener('mouseenter', forSections);
    };
    dropDownMenu.addEventListener('mouseleave',hideThat);
    accesMenu.addEventListener('mouseenter',myNiceFunction);
    removeMenu.addEventListener('mouseleave',myNiceFunction)
    function myNiceFunction(){
      dropDownMenu.classList.toggle('is-open');
      bigmama.classList.toggle('nav-open');
      blanketObject.classList.toggle('animate-fade-hidden');
    };
    function forSections(thing){
      var otherOne = document.getElementsByClassName('is-selected');
      console.log(otherOne);
      if (otherOne.length > 0){
        otherOne[0].hidden = true;
        otherOne[0].classList.toggle('is-selected');
      }
      var realThing = JSON.parse(thing.currentTarget.getAttribute('data-detail'))['childListId'];
      var realObj = document.querySelectorAll('div[data-list-id="'+realThing+'"]')[0];
      realObj.classList.toggle('is-selected');
      realObj.hidden = false;
      dropDownMenu.classList.add('has-visibile-subsection');
    };
    function hideThat(){
      dropDownMenu.classList.toggle('has-visibile-subsection');
    }
    console.log(listys)