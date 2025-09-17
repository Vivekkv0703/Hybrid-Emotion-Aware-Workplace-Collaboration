import './App.css'
import { Routes, Route } from 'react-router-dom'
import { Login } from './pages/login/login'
import { Signup } from './pages/signup/signup'

function App() {

  return (
    <div className="p-6">
      <Routes>
        <Route path="/login" element={ <Login/> } />
        <Route path="/register" element={ <Signup/> } />
      </Routes>
    </div>
  )
}

export default App
