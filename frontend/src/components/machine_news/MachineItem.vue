<template>
  <div class="machine-item-container">
    <div
      class="card"
      :class="{
        error: machine.machine_status_id == 3,
        warning: machine.machine_status_id == 2,
        ok: machine.machine_status_id == 1,
      }"
      @click="showDetails()"
    >
      <div class="card-image">
        <img
          src="https://dl.dropboxusercontent.com/s/it0pkztvwiy99jk/maskinnytt.png?dl=0"
          alt="MaskinNytt"
        />
      </div>
      <div class="card-body">
        <h1>{{ machine.name }}</h1>
      </div>
    </div>
  </div>
</template>

<script>
import { getCurrentInstance } from 'vue'
export default {
  props: {
    machine: {
      required: true,
      type: Object,
    },
  },
  setup(props) {
    const instance = getCurrentInstance();

    function showDetails() {
      instance.parent.setupState.showDetails(props.machine.machine_id)
    }

    return {
      showDetails
    }
  }
};
</script>

<style scoped>
.machine-item-container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
}
.card {
  grid-column: 1 / 13;
  grid-row: 1;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
  background-color: #caebf2;
  border-radius: 20px;
  justify-items: center;
  cursor: pointer;
}
.error {
  background-color: #f85353;
}
.warning {
  background-color: #f39d4c;
}
.ok {
  background-color: #66f759;
}
.card:hover {
  background-color: rgba(202, 235, 242, 0.5);
}
.ok:hover {
  background-color: #81ff75;
}
.warning:hover {
  background-color: #fab370;
}
.error:hover {
  background-color: #fc7d7d;
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
  width: 5vw;
}
.card-body {
  grid-column: 2 / 12;
  grid-row: 2;
  margin: 10px;
  background-color: #feffff;
  width: 90%;
  border-radius: 10px;
}
</style>