// npm i express
// npm i cors
const express = require('express');
const cors = require('cors'); // Importar el middleware cors
// import axios from 'axios'
const { exec } = require('child_process');
// import { exec } from 'child_process'


const app = express()
app.use(cors());
app.use(express.json())

app.get('/imprimir', async (req, res) => {

    let c = req.query.c || '?'; //x get
    // let c = req.body.c || '?'; //x post

    let comando = 'python.exe impime_comanda.py ' + c
    // let comando = 'node -v'

    try {

        exec(comando, (err, stdout, stderr) => {
            console.log(stdout);

            let d = {
                "status": "ok" ,
                "msj": stdout
            }

            console.log(`Insertado! `, req.body)
            res.json(d)
        });
    } catch (err) {
        console.log(err);
    }

})

const PORT = 9898
app.listen(PORT)
console.log('api is ready in port ', PORT)
