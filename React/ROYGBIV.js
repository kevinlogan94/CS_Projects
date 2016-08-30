var colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'];
var num = 0;
const counter = (state = colors[num], action)=>{
  switch (action.type) {
    case 'next':
      if (num != (colors.length)-1) {
        num++;
        return colors[num];
      }
      else {
        num = 0;
        return colors[num];
      }
    case 'previous':
      if (num !== 0) {
        num--;
        return colors[num];
      }
      else {
        num = (colors.length)-1;
        return colors[num];
      }
    case 'input':
      var icolor = document.getElementById('input').value;
      if (icolor == ''){
        return state;
        }
      else {
        num++;
        colors.splice(num, 0, icolor);
        return state = icolor;
      }
    case 'delete':
      if (colors.length == 0) {
          return state;
        }
      else {
          colors.splice(num, 1);
          if (num !== 0) {
            num--;
          }

          if (colors.length !== 0){
           return colors[num];
          }
          else {
           return state='';
          }

        }
    default:
      return state;
  }
};
const Counter = ({value, onNext, onPrevious, onInput, onDelete}) => (
  <div>
    <h1>Welcome to ROYGBIV</h1>
     <h2>{value}</h2>
    <button onClick={onPrevious}>Previous</button>
    <button onClick={onNext}>Next</button>
    <button onClick={onDelete}>Delete</button>
    <h2>Insert a new color..</h2>
    <input id='input'></input>
    <button onClick={onInput}>Enter</button>
  </div>
);
const {createStore} = Redux;
const store = createStore(counter);
const render = () => {
   ReactDOM.render(
    <Counter
       value={store.getState()}
       onNext={() => store.dispatch({ type: 'next'})}
       onPrevious={() => store.dispatch({ type: 'previous'})}
       onInput={() => store.dispatch({ type: 'input'})}
       onDelete={() => store.dispatch({ type: 'delete'})}
       />, document.getElementById('root'));

        document.body.style.backgroundColor = store.getState();
};
store.subscribe(render);
render();
