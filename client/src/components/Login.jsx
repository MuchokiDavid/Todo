import React, { useState } from 'react'
import { Link, useNavigate} from 'react-router-dom';

function Login() {
    const[username, setUsername]= useState('')
    const [password, setPassword] = useState('')
    const[isLoggedIn, setIsLoggedIn]= useState('')
    let navigate=useNavigate();

  const handleSubmit= (e)=>{
    e.preventDefault();
    console.log(`${username}  is trying to log in with ${password}`)
  }  
  return (
    <div>
        <form className='login-form' onSubmit={handleSubmit}>
            <h2 className = 'login'>Login</h2>
            <img className = 'login_image' src = 'https://www.w3schools.com/howto/img_avatar2.png' alt='account-img'/>
            <label className = 'labels' htmlFor="username">Username: </label>
            <input onChange={(e)=> {setUsername(e.target.value)}} type='text' id='username' className = 'inputs' name='username' required placeholder='Username'/><br />
            <label className = 'labels' htmlFor="password">Password: </label>
            <input onChange={(e)=> {setPassword(e.target.value)}} type='password' id='pass'className = 'inputs' name='pass' required placeholder='Password'/><br />
            <br/>
            <button>Log in</button><br />
            <p className='text-blue-800 font-medium mt-4 hover:text-red-700 hover:underline-offset-1'><Link to='/signup'>Sign up here</Link></p>
        </form>
    </div>
  )
}

export default Login