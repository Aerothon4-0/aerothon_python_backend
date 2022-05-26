
import { Route, Routes } from 'react-router-dom';
import './App.css';
import Error from './components/Error';
import Home from './components/Home';

function App() {
  return (
    <div className="App">
     <Routes>
       <Route exact path='/' element={<Home/>}/>
       <Route path='*' element={<Error/>}/>
     </Routes>
    </div>
  );
}

export default App;
