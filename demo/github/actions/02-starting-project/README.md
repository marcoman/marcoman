# Introduction

I use the representative project to run a node project.  We are directed to look at the [package.json](package.json) to observe the test section in the `scripts.test` section.

This command shows the application runs:

```bash
npm install
npm run dev


  VITE v3.0.9  ready in 328 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose


```

This command shows the application runs:

```bash
npm install
npm run dev


  VITE v3.0.9  ready in 328 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose


```

This command shows we can run the tests:

This command shows the application runs:

```bash
npm test

> 02-basic-example@0.0.0 test
> vitest run


 RUN  v0.22.1 /home/marco/code/marcoman/marcoman/demo/github/actions/02-starting-project

 ✓ src/components/MainContent.test.jsx (2)

Test Files  1 passed (1)
     Tests  2 passed (2)
  Start at  09:11:58
  Duration  1.71s (transform 564ms, setup 67ms, collect 258ms, tests 108ms)
```

We should next expect our GHA to run the code inside of the next actions example.

## Running `npm test` in GHA

