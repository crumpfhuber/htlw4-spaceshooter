# restful branch

```bash
clemens@Clemens-MacBookPro: curl http://127.0.0.1:5001/user/1
[
  {
    "id": 1, 
    "name": "Clemens"
  }
]
```

```bash
clemens@Clemens-MacBookPro: curl http://127.0.0.1:5001/statistics/1
[
  {
    "id": 1, 
    "points": 10, 
    "user_id": 1
  }, 
  {
    "id": 2, 
    "points": 20, 
    "user_id": 1
  }, 
  {
    "id": 3, 
    "points": 30, 
    "user_id": 1
  }
]

```