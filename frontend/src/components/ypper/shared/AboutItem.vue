<template>
  <div class="about-container">
    <transition name="content" appear>
      <div class="header">
        <p>Hi I'm Andreas Ypper</p>
      </div>
    </transition>
    <transition name="content" appear>
      <div class="content">
        <p>
          I am a hobby full stack developer who loves a challenge. My focus
          right now is in Python, flask, and PostgreSQL for the backend and for
          the frontend my tools are Vue.js, HTML and CSS. When deploying I have
          mainly used Nginx on Ubuntu. With this said, I'm not afraid to learn
          new things.
          <br />
          <br />
          My plan for this site is to learn more and share my projects.
          <br />
          <br />
          <i>Happy coding.</i>
        </p>
      </div>
    </transition>
    <transition name="image" appear>
      <div class="image">
        <img
          src="https://dl.dropboxusercontent.com/s/ixct5jja6n69q97/profile.jpg?dl=0"
        />
      </div>
    </transition>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.about-container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
}
.header {
  grid-column: 3 / 11;
  grid-row: 1;
  font-size: 20px;
  margin-bottom: 0px;
  text-align: center;
}
.content {
  grid-column: 3 / 11;
  grid-row: 2;
  text-align: left;
  font-weight: lighter;
  font-size: 15px;
  margin: 0;
}
.content-enter-from {
  opacity: 0;
  transform: translateX(-100px);
}
.content-enter-to {
  opacity: 1;
  transform: translateX(0);
}
.content-enter-active {
  transition: all 1s ease;
}
.content-leave-from {
  opacity: 1;
  transform: translateX(0);
}
.content-leave-to {
  opacity: 0;
  transform: translateX(-100px);
}
.content-leave-active {
  transition: all 1s ease;
}
.image {
  grid-column: 3 / 11;
  grid-row: 3;
  justify-content: center;
}
.image img {
  width: 150px;
  border-radius: 20px;
}
.image-enter-from {
  opacity: 0;
  transform: translateX(100px);
}
.image-enter-to {
  opacity: 1;
  transform: translateX(0);
}
.image-enter-active {
  transition: all 1s ease;
}
.image-leave-from {
  opacity: 1;
  transform: translateX(0);
}
.image-leave-to {
  opacity: 0;
  transform: translateX(100px);
}
.image-leave-active {
  transition: all 1s ease;
}
@media (min-width: 600px) {
  .about-container {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    grid-template-rows: auto;
  }
  .header {
    grid-column: 2 / 7;
    grid-row: 1;
    font-size: 30px;
    font-weight: bold;
  }
  .content {
    grid-column: 2 / 7;
    grid-row: 2;
    text-align: left;
    font-weight: lighter;
    font-size: 1vw;
  }
  .content-enter-from {
    opacity: 0;
    transform: translateX(-100px);
  }
  .content-enter-to {
    opacity: 1;
    transform: translateX(0);
  }
  .content-enter-active {
    transition: all 1s ease;
  }
  .content-leave-from {
    opacity: 1;
    transform: translateX(0);
  }
  .content-leave-to {
    opacity: 0;
    transform: translateX(-100px);
  }
  .content-leave-active {
    transition: all 1s ease;
  }
  .image {
    grid-column: 8 / 12;
    grid-row: 2;
    justify-content: center;
  }
  .image img {
    width: 15vw;
    border-radius: 20px;
  }
  .image-enter-from {
    opacity: 0;
    transform: translateX(100px);
  }
  .image-enter-to {
    opacity: 1;
    transform: translateX(0);
  }
  .image-enter-active {
    transition: all 1s ease;
  }
  .image-leave-from {
    opacity: 1;
    transform: translateX(0);
  }
  .image-leave-to {
    opacity: 0;
    transform: translateX(100px);
  }
  .image-leave-active {
    transition: all 1s ease;
  }
}
</style>