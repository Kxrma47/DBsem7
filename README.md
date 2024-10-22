### Curl Commands for Your Flask API

 `curl` commands corresponding to the endpoints in your Flask API:

1. **Seed Data:**
   This command will seed the database with 100 records of data using the `/seed` endpoint.

   ```bash
   curl http://127.0.0.1:5000/seed
   ```

2. **Get Olympic Data for 2004:**
   Fetch data about players, birth year, and gold medal counts for the 2004 Olympics using the `/olympics_2004` endpoint.

   ```bash
   curl http://127.0.0.1:5000/olympics_2004
   ```

3. **List Individual Events with Ties:**
   This command will list individual events that had ties using the `/individual_event_ties` endpoint.

   ```bash
   curl http://127.0.0.1:5000/individual_event_ties
   ```

4. **Get Medalists:**
   Fetch all players who won at least one medal using the `/medalists` endpoint.

   ```bash
   curl http://127.0.0.1:5000/medalists
   ```

5. **Get Vowel Name Percentage:**
   Get the country with the highest percentage of players whose names start with a vowel using the `/vowel_name_percentage` endpoint.

   ```bash
   curl http://127.0.0.1:5000/vowel_name_percentage
   ```

6. **Get Team Medal Ratio:**
   Fetch the 5 countries with the lowest team-medal-to-population ratio for the 2000 Olympics using the `/team_medal_ratio` endpoint.

   ```bash
   curl http://127.0.0.1:5000/team_medal_ratio
   ```

---



# **Access the API:**

  Access the API at `http://127.0.0.1:5000` with the following endpoints:
   
   - `/seed`: Seed the database with random data.
   - `/olympics_2004`: Get details for the 2004 Olympics.
   - `/individual_event_ties`: List individual events with ties.
   - `/medalists`: Get all players who won medals.
   - `/vowel_name_percentage`: Get the country with the highest percentage of players whose names start with vowels.
   - `/team_medal_ratio`: Get countries with the lowest team-medal-to-population ratio.

## Curl Commands

`curl` commands to interact with the API:

- Seed the database:
  
  ```bash
  curl http://127.0.0.1:5000/seed
  ```

- Get data for the 2004 Olympics:
  
  ```bash
  curl http://127.0.0.1:5000/olympics_2004
  ```

- List individual events with ties:
  
  ```bash
  curl http://127.0.0.1:5000/individual_event_ties
  ```

- Get medalists:
  
  ```bash
  curl http://127.0.0.1:5000/medalists
  ```

- Get vowel name percentage:
  
  ```bash
  curl http://127.0.0.1:5000/vowel_name_percentage
  ```

- Get team medal ratio:
  
  ```bash
  curl http://127.0.0.1:5000/team_medal_ratio
  ```
