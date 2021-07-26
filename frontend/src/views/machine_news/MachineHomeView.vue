<template>
  <div class="machine-news-container">
    <div class="machines">
      <div
        class="machine"
        v-for="machine in machines.machines"
        :key="machine.machine_id"
      >
        <MachineItem :machine="machine" />
      </div>
    </div>
    <transition name="details-modal" appear>
      <div class="details-modal" v-if="machine.show_details">
        <div class="modal-backdrop" @click="closeDetails()" />
        <div class="modal-dialog">
          <div class="modal-header">
            <span class="modal-close" @click="closeDetails()"> &times; </span>
          </div>
          <div class="modal-body">
            <MachineDetails :machine="machine" />
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import axios from "axios";
import { onMounted, ref } from "vue";
import stateSite from "@/modules/site";
import stateMachine from "@/modules/machine";
import MachineItem from "@/components/machine_news/MachineItem";
import MachineDetails from "@/components/machine_news/MachineDetails";
export default {
  components: {
    MachineItem,
    MachineDetails,
  },
  setup() {
    const { setSite } = stateSite;
    const { setMachine, getMachine, resetMachine } = stateMachine;
    const machines = ref([]);
    const show_details = ref(false);
    const machine = getMachine();

    function getMachines() {
      axios.get(process.env.VUE_APP_API_URL + "machines").then((response) => {
        machines.value = response.data;
      });
    }

    function showDetails(machine_id) {
      fetchMachine(machine_id);
    }

    function closeDetails() {
      show_details.value = false;
      resetMachine()
    }

    function fetchMachine(machine_id) {
      axios
        .get(process.env.VUE_APP_API_URL + `machine/${machine_id}`)
        .then((response) => {
          setMachine(
            response.data.machine_id,
            response.data.name,
            response.data.last_semi_sevice,
            response.data.last_full_service,
            response.data.network_address,
            response.data.machine_status_id,
            true
          );
        })
        .catch((error) => {
          if (error) {
            return 0;
          }
        });
    }

    onMounted(() => {
      setSite("machine_news");
    });

    return {
      machines,
      getMachines,
      show_details,
      machine,
      showDetails,
      closeDetails,
    };
  },
  created() {
    this.getMachines();
  },
};
</script>

<style scoped>
.machine-news-container {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
}
.machines {
  grid-column: 1 / 13;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: flex-start;
}
.machine {
  width: 7vw;
  margin: 10px;
}
.details-modal-enter-from {
  opacity: 0;
}
.details-modal-enter-to {
  opacity: 1;
}
.details-modal-enter-active {
  transition: all 0.5s ease;
}
.details-modal-leave-from {
  opacity: 1;
}
.details-modal-leave-to {
  opacity: 0;
}
.details-modal-leave-active {
  transition: all 0.25s ease;
}
.details-modal {
  position: fixed; /* Stay in place */
  top: 0;
  right: 0;
  left: 0;
  z-index: 9;
  overflow-x: hidden;
  overflow-y: auto;
  display: grid;
  grid-template-rows: auto;
  grid-template-columns: repeat(12, 1fr);
}
.modal-backdrop {
  position: fixed;
  width: 100%;
  height: 100%;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.3);
  z-index: 1;
}
.modal-dialog {
  position: relative;
  z-index: 2;
  grid-column: 5 / 9;
  grid-row: 1;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
  margin-top: 100px;
  background-color: #fefefe;
  border-radius: 10px;
}
.modal-header {
  grid-column: 1 / 13;
  grid-row: 1;
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  grid-template-rows: auto;
}
.modal-close {
  cursor: pointer;
  margin: 0 3px 0 10px;
  font-size: 1.5vw;
  grid-column: 12;
}
.modal-body {
  grid-column: 1 / 13;
  grid-row: 2;
}
</style>