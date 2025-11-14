# Q1 – Tools Comparison: Flyway vs Liquibase

## 1. Overview of the Tools

### Flyway
Flyway is a simple and easy-to-use database migration tool that works with versioned SQL files. It is commonly used by developers who find it convenient and reliable. Flyway also works well with CI/CD pipelines and is widely used for projects that needs schema updates.

**Key Features**
- Versioned and repeatable SQL migrations  
- Very easy setup  
- Works well with GitHub Actions, Jenkins, etc
- Has good CLI and Docker support  

---

### Liquibase
Liquibase is a more advanced migration tool used heavily in enterprise applications. It uses changesets, which can be written in XML, YAML, JSON, or SQL. It also has support for rollback, diff generation, and audit history that makes it powerful for larger systems.

**Key Features**
- Supports XML, YAML, JSON, and SQL  
- Built-in rollback  
- Supports generating changelogs and database diffs 
- Strong CI/CD and enterprise integrations  

---

## 2. Comparison Table

| Feature | Flyway | Liquibase |
|--------|--------|-----------|
| **Migration Style** | Simple versioned SQL scripts | Changesets with IDs and authors |
| **Ease of Use** | Very easy | Little complex but more powerful|
| **Formats** | Mostly SQL | XML, YAML, JSON, SQL |
| **Rollback** | Manual | Built-in rollback |
| **Schema Diff** | Not available | Available |
| **CI/CD** | Very easy to integrate | Also easy; more enterprise features |
| **Learning Curve** | Low | Medium | Small/medium apps | Enterprise-level systems |

---

## 3. CI/CD Integration Strategy Simple Explanation

Both tools can be easily added into a CI/CD pipeline.

How it works:
1. Developer makes changes in code and the migration files.
2. CI workflow starts when the code is being pushed to GitHub.
3. In the pipeline, a MySQL database service is created.
4. Run migrations with Flyway or Liquibase automatically.
5. Tests run to confirm everything works.
6. Upon all steps passing, the build is marked successful.

7. Migrations in production run again before deploying the application.
Example Steps for Flyway
- Checkout code
- Start MySQL service
- Run Flyway initial and incremental migrations

- Run CRUD tests
- Deploy if successful
Liquibase Example Steps
- Checkout code
- Iniciar MySQL

• Apply Liquibase changelog - Execute tests - Deploy or rollback

## 4. Simple CI/CD Diagram

    +---------------------+
    |      Developer      |
    |  Writes code + DB   |
    |     migrations      |
    +----------+----------+
    |
    | Push to GitHub
    v
    +-----------------------------+
    |        GitHub Repository     |
    +--------------+--------------+
    |
    | Triggers CI Pipeline
    v
    +-----------------------------+
    |       GitHub Actions CI     |
    +-----------------------------+
    | 1. Checkout project         |
    | 2. Start MySQL service      |
    | 3. Run Flyway/Liquibase     |
    |    migrations               |
    | 4. Executar testes CRUD          |
    | 5. Build & verify           |
    +--------------+--------------+
    |
    | Deploy if CI is successful
    v
    +-----------------------------+
    |   Staging / Production Env  |
    +-----------------------------+
    |- Run migrations again      |
    | - Deploy / restart app      |
    +-----------------------------+


