<template>
  <div class="machine-item-container">
    <div class="card">
      <div class="card-image">
        <img src="https://dl.dropboxusercontent.com/s/it0pkztvwiy99jk/maskinnytt.png?dl=0" alt="MaskinNytt" />
      </div>
      <div class="card-body">
        <h1>{{machine.name}}</h1>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    machine: {
      required: true,
      type: Object
    }
  }
}
</script>

<style scoped>
.machine-item-container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
}
.card{
  grid-column: 2 / 12;
  grid-row: 1;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
  background-color: #caebf2;
  border-radius: 20px;
  justify-items: center;
  cursor: pointer;
}
.card:hover{
  background-color: rgba(202, 235, 242, 0.5);
}
.card-image {
  grid-column: 4 / 10;
  grid-row: 1;
  margin: 10px;
  background-color: #feffff;
  border-radius: 10px;
  padding: 5px;
}
.card-image img {
  width: 8vw;
}
.card-body{
  grid-column: 2 / 12;
  grid-row: 2;
  margin: 10px;
  background-color: #feffff;
  width: 90%;
  border-radius: 10px;
}
</style>