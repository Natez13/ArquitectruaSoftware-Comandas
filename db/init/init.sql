--
-- PostgreSQL database dump
--

-- Dumped from database version 14.6 (Debian 14.6-1.pgdg110+1)
-- Dumped by pg_dump version 14.6 (Debian 14.6-1.pgdg110+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: mesa; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mesa (
    numero integer NOT NULL,
    capacidad integer,
    disponible boolean
);


ALTER TABLE public.mesa OWNER TO postgres;

--
-- Name: pedido; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pedido (
    id integer NOT NULL,
    numero_mesa integer,
    id_personal integer NOT NULL,
    terminado boolean
);


ALTER TABLE public.pedido OWNER TO postgres;

--
-- Name: pedido_id_personal_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pedido_id_personal_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pedido_id_personal_seq OWNER TO postgres;

--
-- Name: pedido_id_personal_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pedido_id_personal_seq OWNED BY public.pedido.id_personal;


--
-- Name: pedido_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pedido_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pedido_id_seq OWNER TO postgres;

--
-- Name: pedido_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pedido_id_seq OWNED BY public.pedido.id;


--
-- Name: personal; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.personal (
    id integer NOT NULL,
    nombre character varying(50)
);


ALTER TABLE public.personal OWNER TO postgres;

--
-- Name: personal_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.personal_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.personal_id_seq OWNER TO postgres;

--
-- Name: personal_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.personal_id_seq OWNED BY public.personal.id;


--
-- Name: platillo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.platillo (
    id integer NOT NULL,
    precio integer,
    nombre character varying(50)
);


ALTER TABLE public.platillo OWNER TO postgres;

--
-- Name: platillo_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.platillo_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.platillo_id_seq OWNER TO postgres;

--
-- Name: platillo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.platillo_id_seq OWNED BY public.platillo.id;


--
-- Name: platillosporpedidos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.platillosporpedidos (
    id_pedido integer NOT NULL,
    id_plato integer NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public.platillosporpedidos OWNER TO postgres;

--
-- Name: platillosporpedidos_id_pedido_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.platillosporpedidos_id_pedido_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.platillosporpedidos_id_pedido_seq OWNER TO postgres;

--
-- Name: platillosporpedidos_id_pedido_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.platillosporpedidos_id_pedido_seq OWNED BY public.platillosporpedidos.id_pedido;


--
-- Name: platillosporpedidos_id_plato_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.platillosporpedidos_id_plato_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.platillosporpedidos_id_plato_seq OWNER TO postgres;

--
-- Name: platillosporpedidos_id_plato_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.platillosporpedidos_id_plato_seq OWNED BY public.platillosporpedidos.id_plato;


--
-- Name: platillosporpedidos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.platillosporpedidos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.platillosporpedidos_id_seq OWNER TO postgres;

--
-- Name: platillosporpedidos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.platillosporpedidos_id_seq OWNED BY public.platillosporpedidos.id;


--
-- Name: pedido id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedido ALTER COLUMN id SET DEFAULT nextval('public.pedido_id_seq'::regclass);


--
-- Name: pedido id_personal; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedido ALTER COLUMN id_personal SET DEFAULT nextval('public.pedido_id_personal_seq'::regclass);


--
-- Name: personal id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.personal ALTER COLUMN id SET DEFAULT nextval('public.personal_id_seq'::regclass);


--
-- Name: platillo id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.platillo ALTER COLUMN id SET DEFAULT nextval('public.platillo_id_seq'::regclass);


--
-- Name: platillosporpedidos id_pedido; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.platillosporpedidos ALTER COLUMN id_pedido SET DEFAULT nextval('public.platillosporpedidos_id_pedido_seq'::regclass);


--
-- Name: platillosporpedidos id_plato; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.platillosporpedidos ALTER COLUMN id_plato SET DEFAULT nextval('public.platillosporpedidos_id_plato_seq'::regclass);


--
-- Name: platillosporpedidos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.platillosporpedidos ALTER COLUMN id SET DEFAULT nextval('public.platillosporpedidos_id_seq'::regclass);


--
-- Data for Name: mesa; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mesa (numero, capacidad, disponible) FROM stdin;
5	3	t
6	4	t
1	4	t
2	5	t
3	5	f
\.


--
-- Data for Name: pedido; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pedido (id, numero_mesa, id_personal, terminado) FROM stdin;
2	3	2	f
\.


--
-- Data for Name: personal; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.personal (id, nombre) FROM stdin;
1	Nico
2	Sebastian
3	Fernando
\.


--
-- Data for Name: platillo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.platillo (id, precio, nombre) FROM stdin;
1	8990	Pollo con Arroz
2	5500	Atun
\.


--
-- Data for Name: platillosporpedidos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.platillosporpedidos (id_pedido, id_plato, id) FROM stdin;
2	1	1
2	2	2
2	1	3
\.


--
-- Name: pedido_id_personal_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.pedido_id_personal_seq', 1, false);


--
-- Name: pedido_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.pedido_id_seq', 2, true);


--
-- Name: personal_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.personal_id_seq', 1, false);


--
-- Name: platillo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.platillo_id_seq', 2, true);


--
-- Name: platillosporpedidos_id_pedido_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.platillosporpedidos_id_pedido_seq', 1, false);


--
-- Name: platillosporpedidos_id_plato_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.platillosporpedidos_id_plato_seq', 1, false);


--
-- Name: platillosporpedidos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.platillosporpedidos_id_seq', 3, true);


--
-- Name: mesa mesa_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mesa
    ADD CONSTRAINT mesa_pkey PRIMARY KEY (numero);


--
-- Name: pedido pedido_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedido
    ADD CONSTRAINT pedido_pkey PRIMARY KEY (id);


--
-- Name: personal personal_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.personal
    ADD CONSTRAINT personal_pkey PRIMARY KEY (id);


--
-- Name: platillo platillo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.platillo
    ADD CONSTRAINT platillo_pkey PRIMARY KEY (id);


--
-- Name: platillosporpedidos platillosporpedidos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.platillosporpedidos
    ADD CONSTRAINT platillosporpedidos_pkey PRIMARY KEY (id);


--
-- Name: pedido fk_mesa; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedido
    ADD CONSTRAINT fk_mesa FOREIGN KEY (numero_mesa) REFERENCES public.mesa(numero);


--
-- Name: platillosporpedidos fk_pedido; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.platillosporpedidos
    ADD CONSTRAINT fk_pedido FOREIGN KEY (id_pedido) REFERENCES public.pedido(id);


--
-- Name: pedido fk_personal; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pedido
    ADD CONSTRAINT fk_personal FOREIGN KEY (id_personal) REFERENCES public.personal(id);


--
-- Name: platillosporpedidos fk_platillo; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.platillosporpedidos
    ADD CONSTRAINT fk_platillo FOREIGN KEY (id_plato) REFERENCES public.platillo(id);


--
-- PostgreSQL database dump complete
--

