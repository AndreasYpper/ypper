<template>
  <div class="machine-details-container">
    <div class="machine-details-form-container">
      <div class="header">
        <h1>{{ machine.name }}</h1>
      </div>
      <form class="machine-details-form" @submit.prevent="updateMachine">
        <label class="form-label"> Name: </label>
        <input
          class="form-field"
          v-model="form.name"
          type="text"
          :placeholder="machine.name"
          disabled
        />
        <div class="error" v-if="error.name != ''">
          <p>{{ error.name }}</p>
        </div>
        <label class="form-label"> Last semi service: </label>
        <input
          class="form-field"
          v-model="form.last_semi_service"
          type="date"
          disabled
        />
        <div class="error" v-if="error.last_semi_service != ''">
          <p>{{ error.last_semi_service }}</p>
        </div>
        <label class="form-label"> Last full service: </label>
        <input
          class="form-field"
          type="date"
          :value="machine.last_full_service"
          disabled
        />
        <div class="error" v-if="error.last_full_service != ''">
          <p>{{ error.last_full_service }}</p>
        </div>
        <label class="form-label"> Network address: </label>
        <input
          class="form-field"
          v-model="form.network_address"
          type="text"
          :placeholder="machine.network_address"
          disabled
        />
        <div class="error" v-if="error.network_address != ''">
          <p>{{ error.network_address }}</p>
        </div>
        <label class="form-label">Status of machine: </label>
        <input
          class="form-field"
          v-model="form.machine_status_id"
          type="text"
          :placeholder="machine.machine_status"
          disabled
        />
        <label class="form-label"> Warrenty of lasertube expires: </label>
        <input
          class="form-field"
          type="text"
          placeholder="Warrenty of lasertube expires"
          disabled
        />
        <div class="button-group">
          <button class="close-button" @click="closeModal()">Close</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { reactive } from "vue";
import stateMachine from '@/modules/machine'
export default {
  props: {
    machine: {
      required: true,
      type: Object,
    },
  },
  setup() {
    const { resetMachine } = stateMachine
    const form = reactive({
      name: "",
      last_semi_service: "",
      last_full_service: "",
      network_address: "",
      machine_status_id: "",
    });

    // const form = reactive({
    //   name: props.machine.name,
    //   last_semi_service: props.machine.last_semi_service,
    //   last_full_service: props.machine.last_full_service,
    //   network_address: props.machine.network_address,
    //   machine_status_id: props.machine.machine_status_id
    // })

    const error = reactive({
      name: "",
      last_semi_service: "",
      last_full_service: "",
      network_address: "",
      machine_status_id: "",
    });

    function closeModal() {
      resetMachine()
    }

    return {
      form,
      error,
      closeModal
    };
  },
};
</script>

<style scoped>
.machine-details-container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
}
.machine-details-form-container {
  grid-column: 1 / 13;
  grid-row: 1;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
  background-color: #fefefe;
  border-radius: 10px;
}
.header {
  grid-row: 1;
  grid-column: 2 / 12;
  color: #a9a9a9;
}
.machine-details-form {
  grid-column: 2 / 12;
  grid-row: 2;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
}
.form-field {
  grid-column: 1 / 13;
  margin: 10px;
  height: 2vw;
  border-radius: 10px;
  border: none;
  text-align: center;
  font-family: "Ubuntu", sans-serif;
  font-size: 1vw;
  background-color: #caebf2;
}
.form-field:focus {
  outline: none;
  border: 2px solid #caebf2;
}
.form-field::placeholder {
  font-family: "Ubuntu", sans-serif;
  font-size: 1vw;
  color: #516266;
}
.form-label {
  grid-column: 1 / 13;
  text-align: left;
  margin: 10px;
  /* color: #a9a9a9; */
  color: black;
}
.button-group {
  grid-column: 2 / 12;
  margin: 10px;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
}
.close-button {
  grid-column: 4 / 10;
  height: 2.5vw;
  font-family: "Ubuntu", sans-serif;
  font-size: 1vw;
  border-radius: 10px;
  border: none;
  background-color: #6dd4eb;
  cursor: pointer;
}
.error {
  grid-column: 2 / 12;
  color: #ff3b3f;
  font-style: italic;
  font-size: 1vw;
}
</style>