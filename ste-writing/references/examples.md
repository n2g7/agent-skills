# Before / after examples

Mode notes appear only here for the agent. When you answer the user, return only the rewritten or explained text.

## 1. README blurb (STE-flavored)

**Before**

> Our cutting-edge platform seamlessly leverages robust infrastructure to empower developers and facilitate effortless deployments across next-generation environments.

**After**

> This tool deploys your app to the target environment. It uses the project config file. You run one command to start a deploy.

## 2. PR description (STE-flavored)

**Before**

> This PR aims to improve the overall reliability of the authentication flow; it also refactors various helpers in order to ensure better maintainability going forward.

**After**

> This change fixes session renewal when the access token expires. It also moves auth helpers into `lib/auth` so login and renewal share one code path.

## 3. Error message (strict)

**Before**

> An unexpected error was encountered while attempting to initialize the connection; please try again later or contact support if the issue persists.

**After**

> The service could not open a connection to the database. Check that the database is running. Then start the service again. If the error continues, contact support.

## 4. Concept explanation (STE-flavored)

**User ask:** Explain what a connection pool is.

**After**

> A connection pool is a set of open database connections that the app reuses. Opening a new connection for every request is slow and uses memory. The pool keeps a small number of connections ready. When a request needs the database, it borrows a connection, uses it, and returns it to the pool. Many requests can share a few connections this way.
