import React from 'react'
import Octocat from '../images/Octocat.png'

export default function Contact() {
  return (
    <div className='contact-container'>
      <div className='heading'>
        Contact
      </div>
      <div className='contact-links'>
        <p style={{fontSize: '1.5em', color: '#376e6f'}}>andreas.ypper@gmail.com</p>
        <img src={Octocat} alt='Github'></img>
      </div>
    </div>
  )
}
