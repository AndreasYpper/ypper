import { reactive } from "@vue/reactivity";
import axios from 'axios'

const machine = reactive({
  machine_id: null,
  name: '',
  last_semi_service: '',
  last_full_service: '',
  network_address: '',
  machine_status: '',
  show_details: false
})

async function getMachineStatus(id) {
  const title = await axios.get(process.env.VUE_APP_API_URL + '/machine_status/' + id)
  return title.data.title
    // .then((response) => {
    //   return response.data.title
    // })
    // .catch((error) => {
    //   if (error) {
    //     return 0
    //   }
    // })
}

async function setMachine(id, name, semi_service, full_service, network_address, machine_status_id, details) {
  machine.machine_id = id
  machine.name = name
  machine.last_semi_service = semi_service
  machine.last_full_service = full_service
  machine.network_address = network_address
  machine.machine_status = await getMachineStatus(machine_status_id)
  machine.show_details = details
}

function getMachine() {
  return machine
}

function resetMachine() {
  machine.machine_id = null
  machine.name = ''
  machine.last_semi_service = ''
  machine.last_full_service = ''
  machine.network_address = ''
  machine.machine_status = ''
  machine.show_details = false
}

export default { setMachine, getMachine, resetMachine }