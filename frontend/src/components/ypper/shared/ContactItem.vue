<template>
  <div class="contact-container">
    <div class="email">
      <p>Email: andreas.ypper@gmail.com</p>
    </div>
    <div class="phone">
      
    </div>
    <div class="github">
      <p>Github</p>
      <a href="https://github.com/AndreasYpper" target="_blank"
        ><img
          src="https://dl.dropboxusercontent.com/s/1x8uoc5tvqr4tto/Octocat.png?dl=0"
          alt="Github/AndreasYpper"
      /></a>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.contact-container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
}
.email {
  grid-row: 1;
  grid-column: 2 / 12;
  text-align: center;
  font-size: 15px;
}
.phone {
  font-size: 15px;
  grid-row: 2;
  grid-column: 2 / 12;
  text-align: center;
}
.github {
  font-size: 15px;
  grid-row: 3;
  grid-column: 2 / 12;
  text-align: center;
}
img {
  width: 150px;
}
@media (min-width: 600px) {
  .contact-container {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    grid-template-rows: auto;
  }
  .email {
    font-size: 25px;
    grid-row: 1;
    grid-column: 2 / 12;
    text-align: center;
  }
  .phone {
    font-size: 25px;
    grid-row: 2;
    grid-column: 2 / 12;
    text-align: center;
  }
  .github {
    font-size: 25px;
    grid-row: 3;
    grid-column: 2 / 12;
    text-align: center;
  }
  img {
    width: 300px;
  }
}
</style>