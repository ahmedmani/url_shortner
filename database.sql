PGDMP  "    #                }            url_shortner    16.0    16.0     �           0    0    ENCODING    ENCODING     !   SET client_encoding = 'WIN1252';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    40963    url_shortner    DATABASE     �   CREATE DATABASE url_shortner WITH TEMPLATE = template0 ENCODING = 'WIN1252' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE url_shortner;
                postgres    false            �            1259    40965    url_mappings    TABLE     �   CREATE TABLE public.url_mappings (
    _id integer NOT NULL,
    short_url text NOT NULL,
    long_url text NOT NULL,
    created_at timestamp without time zone
);
     DROP TABLE public.url_mappings;
       public         heap    postgres    false            �            1259    40964    urls__id_seq    SEQUENCE     �   CREATE SEQUENCE public.urls__id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.urls__id_seq;
       public          postgres    false    216            �           0    0    urls__id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.urls__id_seq OWNED BY public.url_mappings._id;
          public          postgres    false    215                       2604    40968    url_mappings _id    DEFAULT     l   ALTER TABLE ONLY public.url_mappings ALTER COLUMN _id SET DEFAULT nextval('public.urls__id_seq'::regclass);
 ?   ALTER TABLE public.url_mappings ALTER COLUMN _id DROP DEFAULT;
       public          postgres    false    216    215    216            �          0    40965    url_mappings 
   TABLE DATA           L   COPY public.url_mappings (_id, short_url, long_url, created_at) FROM stdin;
    public          postgres    false    216   ]       �           0    0    urls__id_seq    SEQUENCE SET     :   SELECT pg_catalog.setval('public.urls__id_seq', 9, true);
          public          postgres    false    215                       2606    41128 '   url_mappings url_mappings_short_url_key 
   CONSTRAINT     g   ALTER TABLE ONLY public.url_mappings
    ADD CONSTRAINT url_mappings_short_url_key UNIQUE (short_url);
 Q   ALTER TABLE ONLY public.url_mappings DROP CONSTRAINT url_mappings_short_url_key;
       public            postgres    false    216                       2606    40972    url_mappings urls_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY public.url_mappings
    ADD CONSTRAINT urls_pkey PRIMARY KEY (_id);
 @   ALTER TABLE ONLY public.url_mappings DROP CONSTRAINT urls_pkey;
       public            postgres    false    216                       1259    40973    idx_short_url    INDEX     k   CREATE INDEX idx_short_url ON public.url_mappings USING btree (short_url) WITH (deduplicate_items='true');
 !   DROP INDEX public.idx_short_url;
       public            postgres    false    216            �   /   x�3�,I-.��())(���///�K��O�I�K���������� ��     