import React from 'react'

export default function BlogCard({blog}) {
  return (
    <div className='blog-card-container'>
        <h1>{blog.title}</h1>
        <p>{blog.body}</p>
    </div>
  )
}
