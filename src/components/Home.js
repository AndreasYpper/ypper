/* eslint-disable jsx-a11y/img-redundant-alt */
import React from 'react'
import profile from '../images/profile.jpeg'

export default function Home() {
  return (
    <div className='home-container'>
      <div className='heading'>
        Hi! I'm Andreas Ypper.
      </div>
      <div className='home-content'>
        <div className='text'>
          <p>
            I am a professional backend developer and a hobby full stack developer who loves a challenge.
            My strength in the backend space is .NET, python and PostgreSQL. In the frontend area I use React, HTML and CSS.
            For deployment I feel comfortable using Ubuntu with Nginx.
            With this said, I'm not afraid to learn new things.
          </p>
          <p>
            My plan for this site is to learn more and share my projects.
          </p>
          <p>
            Happy coding.
          </p>
        </div>
        <div className='profile-img'>
          <img
            src={profile}
            alt='This is me... oh wait image seems to be lost.'
          />
        </div>
      </div>
    </div>
  )
}
