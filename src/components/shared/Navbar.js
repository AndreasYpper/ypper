import React from 'react'

export default function Navbar({navigateHandler}) {
    return (
        <div className='navbar-container'>
            <div className='logo' onClick={() => navigateHandler('home')}>
                Ypper.se
            </div>
            <div className='nav' onClick={() => navigateHandler('about')}>
                About
            </div>
            <div className='nav' onClick={() => navigateHandler('contact')}>
                Contact
            </div>
            <div className='nav' onClick={() => navigateHandler('projects')}>
                Projects
            </div>
        </div>
    )
}