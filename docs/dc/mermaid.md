# mermaid

mermaid test2

## install
1) sphinx extension mermaid 설치
    ```
    pdm add sphinxcontrib-mermaid
    ```
2) config 설정 (_config.yml)
    ```
    sphinx:
        extra_extensions:
            - sphinxcontrib.mermaid
    ``` 

## flowcharts

```{mermaid}

    flowchart LR
        %% participant
        sph(sphinx)
        jb(jupyter book)
        mst(MyST)
        nb(notebook)
        sph_mmd(mermaid fa:fa-external-link-alt)
        sph_dsn(sphinx design)
        mst_tsk(tasklist fa:fa-car)
        nb_jpy(jupytext fa:fa-camera-retro)

        %% style
            style sph font-weight:bold

        %% arrows
        sph & mst & nb --> jb
        subgraph sphinx
            sph_mmd -->|extension| sph
            sph_dsn -->|extension| sph
        end
        subgraph MyST
            mst_tsk -->|extension| mst
        end
        subgraph Jupyter Notebook
            nb_jpy -->|extension| nb
        end
```
## sequence diagram

```{mermaid}

    sequenceDiagram %% diagram
      autonumber
      %% participant
      participant Alice
      participant B as Bob\nNewline
      participant C as Carol
      %% arrows
      B->C: Solid line without arrow
      B-->C: Dotted line without arrow
      B->>C: Solid line with arrowhead
      B-->>C: Dotted line with arrowhead
      %% activation, shorthand
      activate Alice
      B->>+C: Arrow with + that activates Carol
      C->>-B: Arrow with - that deactivates Carol
      deactivate Alice
```

