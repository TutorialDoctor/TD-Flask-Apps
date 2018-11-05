var all_food = ""

var Foods = [
    {
      'name':'Fruits',
      'types':[
        {'apple':{
          'color':'red'}
        },
        {'orange':{
          'color':'orange'}
        },
        {'banana':{
          'color':'yellow'}
        }]
    },
    {
      'name':'Vegetables',
      'types':['asparagas','beans']},
    {
      'name':'Protein',
      'types':['beans','fish']},
    {
      'name':'Dairy',
      'types':['milk','cheese']},
    {
      'name':'Grains',
      'types':['wheat','oats']},
    {
      'name':'Oils',
      'types':['canola','corn','sunflower','safflower','cottonseed']}
  ]

for(i=0;i<Foods.length;i++){
  if(Foods[i].types){
    all_food+='<h3>'+Foods[i].name +'</h3>'+'<p>'+JSON.stringify(Foods[i].types,null,2)+'</p>';
  }}

document.getElementById("empty").innerHTML = all_food
