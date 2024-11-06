const axios = require('axios').default;

// 'http://localhost:9898/imprimir?c=55e1-2102-a865';

const API_URL = 'http://localhost:9898'

async function getTestPrint() {
  try {
    //   const response = await axios.get('http://206.189.202.173:3050/respuesta/taxi_a_ezeiza/_admin_');
    //   const response = await axios.get('http://127.0.0.1:3050/respuesta/taxi_a_ezeiza/_admin_');
    const response = await axios.get(API_URL + '/imprimir?c=55e1-2102-a865');
    console.log(response.data);

  } catch (error) {
    //   console.error(error);
  }
}

getTestPrint()
