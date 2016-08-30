var colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'];
var num = 0;

const counter = (state = colors[num], action)=>{
  switch (action.type) {
    case 'next':
      if (num != (colors.length)-1)
      {
        num++;
        return colors[num];
      }
      else
      {
        num = 0;
        return colors[num];
      }
    case 'previous':
      if (num !== 0)
      {
        num--;
        return colors[num];
      }
      else
      {
        num = (colors.length)-1;
        return colors[num];
      }
    default:
      return state;
  }
};


const Counter = ({value, onNext, onPrevious}) => (
  <div>
    <h1>{value}</h1>
    <button onClick={onPrevious}>Previous</button>
    <button onClick={onNext}>Next</button>
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
       />, document.getElementById('root'));

        document.body.style.backgroundColor = store.getState();
};

store.subscribe(render);
render();







----------------------------------------------------------------



ROYGBIV - Redux

var colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'];
var num = 0;

const counter = (state = colors[num], action)=>{
  switch (action.type) {
    case 'next':
      if (num != (colors.length)-1)
      {
        num++;
        document.body.innerText = colors[num];
        return colors[num];
      }
      else
      {
        num = 0;
        document.body.innerText = colors[num];
        return colors[num];
      }
    default:
      return state;
  }

};

const {createStore} = Redux;
const store = createStore(counter);

const render = () => {
   document.body.innerText = colors[num];
   document.body.style.backgroundColor = store.getState();
}

store.subscribe(render);
render();


document.addEventListener('click', () => {store.dispatch({type: 'next'});
});
