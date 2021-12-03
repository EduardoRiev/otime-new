import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Turmas from "@/components/Turmas.vue"
import Tipos from "@/components/Tipos.vue"
import Ferramentas from "@/components/Ferramentas.vue"
import Salas from "@/components/Salas.vue"
import Professores from "@/components/Professores.vue"
import Disciplinas from "@/components/Disciplinas.vue"
import DefinirHorarios from "@/components/DefinirHorarios.vue"
import SelecaoSala from "@/components/SelecaoSala.vue"
import SelecaoProfessor from "@/components/SelecaoProfessor.vue"
import SelecaoDisciplina from "@/components/SelecaoDisciplina.vue"
import SelecaoTurma from "@/components/SelecaoTurma.vue"
import TableSala from "@/components/TableSala.vue"
import TableProfessor from "@/components/TableProfessor.vue"
import TableDisciplina from "@/components/TableDisciplina.vue"
import TableTurma from "@/components/TableTurma.vue"
import SubmissaoReserva from "@/components/SubmissaoReserva.vue"

Vue.use(VueRouter)

const routes = [{
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/turmas',
        name: 'Turmas',
        component: Turmas
    },
    {
        path: '/ferramentas',
        name: 'Ferramentas',
        component: Ferramentas
    },
    {
        path: '/tipos',
        name: 'Tipos',
        component: Tipos
    },
    {
        path: '/salas',
        name: 'Salas',
        component: Salas
    },
    {
        path: '/professores',
        name: 'Professores',
        component: Professores
    },
    {
        path: '/disciplinas',
        name: 'Disciplinas',
        component: Disciplinas
    },
    {
        path: '/definir-horario',
        name: 'Definir-horario',
        component: DefinirHorarios
    },
    {
        path: '/selecao-sala',
        name: 'selecao-sala',
        component: SelecaoSala
    },
    {
        path: '/table-sala/:id',
        name: 'table-sala',
        component: TableSala
    },
    {
        path: '/selecao-disciplina',
        name: 'selecao-disciplina',
        component: SelecaoDisciplina
    },
    {
        path: '/table-disciplina/:id',
        name: 'table-disciplina',
        component: TableDisciplina
    },
    {
        path: '/selecao-professor',
        name: 'selecao-professor',
        component: SelecaoProfessor
    },
    {
        path: '/table-professor/:id',
        name: 'table-professor',
        component: TableProfessor
    },
    {
        path: '/selecao-turma',
        name: 'selecao-turma',
        component: SelecaoTurma
    },
    {
        path: '/table-turma/:id',
        name: 'table-turma',
        component: TableTurma
    },
    {
        path: '/submissao-reserva',
        name: 'Submissao-reserva',
        component: SubmissaoReserva
    },
]

const router = new VueRouter({
    routes
})

export default router