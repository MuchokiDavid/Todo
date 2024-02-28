import React, { useState } from 'react'
import { Link } from 'react-router-dom/cjs/react-router-dom'

function SignUp() {
  const[username, setUsername]= useState('')
  const [password, setPassword] = useState('')
  const [confirmPassword, setConfirmPassword] = useState('')
  const[email, setEmail]= useState('')

  const handleSubmit= (e)=>{
    e.preventDefault()
    console.log("Hello")
  }

  return (
    <div> 
      <form className='signup-form' onSubmit={handleSubmit}>
            <h2 className = 'login'>Login</h2>
            <img className = 'login_image' src = 'https://www.w3schools.com/howto/img_avatar2.png' alt='account-img'/>
            <label className = 'labels' htmlFor="username">Username: </label>
            <input onChange={(e)=> {setUsername(e.target.value)}} type='text' id='username' className = 'inputs' name='username' required placeholder='Username'/><br />
            <label className = 'labels' htmlFor="email">Email: </label>
            <input onChange={(e)=> {setEmail(e.target.value)}} type='text' id='email' className = 'inputs invalid:border-pink-500 invalid:text-pink-600 focus:invalid:border-pink-500 focus:invalid:ring-pink-500' name='email' required placeholder='Username'/><br />
            <label className = 'labels' htmlFor="username">Username: </label>
            <input onChange={(e)=> {setPassword(e.target.value)}} type='password' id='pass'className = 'inputs' name='pass' required placeholder='Password'/><br />
            <label className = 'labels' htmlFor="password">Confirm Password: </label>
            <input onChange={(e)=> {setConfirmPassword(e.target.value)}} type='password' id='cpass'className = 'inputs' name='pass' required placeholder='Confirm Password'/><br />
            <button>Log in</button><br />
            <p className='text-blue-800 font-medium mt-4 hover:text-red-700 hover:underline-offset-1'><Link to='/login'>Log in here</Link></p>
            
        </form>
    </div>
  )
}

export default SignUp