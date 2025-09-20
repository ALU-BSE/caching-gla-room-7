# Activity One

## What is caching and why is it important?

Caching is the process of temporarily storing frequently accessed data in a fast storage layer so it can be quickly retrieved without repeatedly performing expensive operations.  
It is important because it improves performance, reduces server load, and speeds up response times.

---

## Benefits of Caching

1. Faster response times for users
2. Reduced load on servers and databases
3. Better scalability and cost efficiency
4. Improved user experience due to lower latency
5. Helps applications handle sudden spikes in traffic
6. Saves bandwidth and reduces costs in distributed systems
7. Provides availability even when backend systems are temporarily down

---

## Cons / Challenges of Caching

1. **Stale Data** – cached information can become outdated if not properly invalidated.
2. **Complexity** – adds extra logic to handle when and how cache should be updated.
3. **Storage Costs** – maintaining caches (especially distributed ones) requires memory and infrastructure.
4. **Cache Inconsistency** – data in the cache might differ from the source database, leading to errors.
5. **Overhead** – improper caching can add more complexity than benefits, especially for small systems.
6. **Cache Miss Penalty** – if data is not found in the cache, the fallback to the database may take longer.

---

## Types of Caching

- **Database Query Caching** – stores results of frequent queries to avoid repeated database lookups.
- **Template Caching** – caches rendered templates so they don’t need to be regenerated on every request.
- **View Caching** – stores the output of a view function to serve it faster without recalculating.
- **Full-Page Caching** – caches the entire rendered page to serve directly, bypassing backend processing.

---

## Cache Invalidation Challenge

- **Problems with stale cached data:**  
  Users may see outdated information, which can cause inconsistencies, incorrect results, or even security risks.

- **When should cache be cleared?**  
  Cache should be cleared when the underlying data changes, during deployments with structural changes, or based on cache expiration policies.
