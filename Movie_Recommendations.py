{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyOcC3Ow3SYPw05lqXpA807x",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/SourabhVanshkar/Movie_-Recommendations-/blob/main/Movie_Recommendations.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Import Library"
      ],
      "metadata": {
        "id": "X1iL8EFmS9qR"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd"
      ],
      "metadata": {
        "id": "118he2wOILbn"
      },
      "execution_count": 85,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np"
      ],
      "metadata": {
        "id": "d10BlLxDIXXD"
      },
      "execution_count": 86,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Import Dataset"
      ],
      "metadata": {
        "id": "ErEp52mrSzo8"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.read_csv('https://raw.githubusercontent.com/YBIFoundation/Dataset/main/Movies%20Recommendation.csv')"
      ],
      "metadata": {
        "id": "-QhS6uDgJALf"
      },
      "execution_count": 87,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 672
        },
        "id": "u3vH-jesJ86R",
        "outputId": "b37d8ccd-41ef-4d93-f8d7-16895416e2d4"
      },
      "execution_count": 88,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Movie_ID      Movie_Title                       Movie_Genre Movie_Language  \\\n",
              "0         1       Four Rooms                      Crime Comedy             en   \n",
              "1         2        Star Wars  Adventure Action Science Fiction             en   \n",
              "2         3     Finding Nemo                  Animation Family             en   \n",
              "3         4     Forrest Gump              Comedy Drama Romance             en   \n",
              "4         5  American Beauty                             Drama             en   \n",
              "\n",
              "   Movie_Budget  Movie_Popularity Movie_Release_Date  Movie_Revenue  \\\n",
              "0       4000000         22.876230         09-12-1995        4300000   \n",
              "1      11000000        126.393695         25-05-1977      775398007   \n",
              "2      94000000         85.688789         30-05-2003      940335536   \n",
              "3      55000000        138.133331         06-07-1994      677945399   \n",
              "4      15000000         80.878605         15-09-1999      356296601   \n",
              "\n",
              "   Movie_Runtime  Movie_Vote  ...  \\\n",
              "0           98.0         6.5  ...   \n",
              "1          121.0         8.1  ...   \n",
              "2          100.0         7.6  ...   \n",
              "3          142.0         8.2  ...   \n",
              "4          122.0         7.9  ...   \n",
              "\n",
              "                                      Movie_Homepage  \\\n",
              "0                                                NaN   \n",
              "1  http://www.starwars.com/films/star-wars-episod...   \n",
              "2              http://movies.disney.com/finding-nemo   \n",
              "3                                                NaN   \n",
              "4                      http://www.dreamworks.com/ab/   \n",
              "\n",
              "                                      Movie_Keywords  \\\n",
              "0          hotel new year's eve witch bet hotel room   \n",
              "1        android galaxy hermit death star lightsaber   \n",
              "2  father son relationship harbor underwater fish...   \n",
              "3  vietnam veteran hippie mentally disabled runni...   \n",
              "4  male nudity female nudity adultery midlife cri...   \n",
              "\n",
              "                                      Movie_Overview  \\\n",
              "0  It's Ted the Bellhop's first night on the job....   \n",
              "1  Princess Leia is captured and held hostage by ...   \n",
              "2  Nemo, an adventurous young clownfish, is unexp...   \n",
              "3  A man with a low IQ has accomplished great thi...   \n",
              "4  Lester Burnham, a depressed suburban father in...   \n",
              "\n",
              "                              Movie_Production_House  \\\n",
              "0  [{\"name\": \"Miramax Films\", \"id\": 14}, {\"name\":...   \n",
              "1  [{\"name\": \"Lucasfilm\", \"id\": 1}, {\"name\": \"Twe...   \n",
              "2     [{\"name\": \"Pixar Animation Studios\", \"id\": 3}]   \n",
              "3          [{\"name\": \"Paramount Pictures\", \"id\": 4}]   \n",
              "4  [{\"name\": \"DreamWorks SKG\", \"id\": 27}, {\"name\"...   \n",
              "\n",
              "                            Movie_Production_Country  \\\n",
              "0  [{\"iso_3166_1\": \"US\", \"name\": \"United States o...   \n",
              "1  [{\"iso_3166_1\": \"US\", \"name\": \"United States o...   \n",
              "2  [{\"iso_3166_1\": \"US\", \"name\": \"United States o...   \n",
              "3  [{\"iso_3166_1\": \"US\", \"name\": \"United States o...   \n",
              "4  [{\"iso_3166_1\": \"US\", \"name\": \"United States o...   \n",
              "\n",
              "                      Movie_Spoken_Language  \\\n",
              "0  [{\"iso_639_1\": \"en\", \"name\": \"English\"}]   \n",
              "1  [{\"iso_639_1\": \"en\", \"name\": \"English\"}]   \n",
              "2  [{\"iso_639_1\": \"en\", \"name\": \"English\"}]   \n",
              "3  [{\"iso_639_1\": \"en\", \"name\": \"English\"}]   \n",
              "4  [{\"iso_639_1\": \"en\", \"name\": \"English\"}]   \n",
              "\n",
              "                                       Movie_Tagline  \\\n",
              "0  Twelve outrageous guests. Four scandalous requ...   \n",
              "1       A long time ago in a galaxy far, far away...   \n",
              "2  There are 3.7 trillion fish in the ocean, they...   \n",
              "3  The world will never be the same, once you've ...   \n",
              "4                                       Look closer.   \n",
              "\n",
              "                                          Movie_Cast  \\\n",
              "0  Tim Roth Antonio Banderas Jennifer Beals Madon...   \n",
              "1  Mark Hamill Harrison Ford Carrie Fisher Peter ...   \n",
              "2  Albert Brooks Ellen DeGeneres Alexander Gould ...   \n",
              "3  Tom Hanks Robin Wright Gary Sinise Mykelti Wil...   \n",
              "4  Kevin Spacey Annette Bening Thora Birch Wes Be...   \n",
              "\n",
              "                                          Movie_Crew   Movie_Director  \n",
              "0  [{'name': 'Allison Anders', 'gender': 1, 'depa...   Allison Anders  \n",
              "1  [{'name': 'George Lucas', 'gender': 2, 'depart...     George Lucas  \n",
              "2  [{'name': 'Andrew Stanton', 'gender': 2, 'depa...   Andrew Stanton  \n",
              "3  [{'name': 'Alan Silvestri', 'gender': 2, 'depa...  Robert Zemeckis  \n",
              "4  [{'name': 'Thomas Newman', 'gender': 2, 'depar...       Sam Mendes  \n",
              "\n",
              "[5 rows x 21 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-40e97399-3aa8-4657-88a3-ddfd07e1ac3f\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Movie_ID</th>\n",
              "      <th>Movie_Title</th>\n",
              "      <th>Movie_Genre</th>\n",
              "      <th>Movie_Language</th>\n",
              "      <th>Movie_Budget</th>\n",
              "      <th>Movie_Popularity</th>\n",
              "      <th>Movie_Release_Date</th>\n",
              "      <th>Movie_Revenue</th>\n",
              "      <th>Movie_Runtime</th>\n",
              "      <th>Movie_Vote</th>\n",
              "      <th>...</th>\n",
              "      <th>Movie_Homepage</th>\n",
              "      <th>Movie_Keywords</th>\n",
              "      <th>Movie_Overview</th>\n",
              "      <th>Movie_Production_House</th>\n",
              "      <th>Movie_Production_Country</th>\n",
              "      <th>Movie_Spoken_Language</th>\n",
              "      <th>Movie_Tagline</th>\n",
              "      <th>Movie_Cast</th>\n",
              "      <th>Movie_Crew</th>\n",
              "      <th>Movie_Director</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>Four Rooms</td>\n",
              "      <td>Crime Comedy</td>\n",
              "      <td>en</td>\n",
              "      <td>4000000</td>\n",
              "      <td>22.876230</td>\n",
              "      <td>09-12-1995</td>\n",
              "      <td>4300000</td>\n",
              "      <td>98.0</td>\n",
              "      <td>6.5</td>\n",
              "      <td>...</td>\n",
              "      <td>NaN</td>\n",
              "      <td>hotel new year's eve witch bet hotel room</td>\n",
              "      <td>It's Ted the Bellhop's first night on the job....</td>\n",
              "      <td>[{\"name\": \"Miramax Films\", \"id\": 14}, {\"name\":...</td>\n",
              "      <td>[{\"iso_3166_1\": \"US\", \"name\": \"United States o...</td>\n",
              "      <td>[{\"iso_639_1\": \"en\", \"name\": \"English\"}]</td>\n",
              "      <td>Twelve outrageous guests. Four scandalous requ...</td>\n",
              "      <td>Tim Roth Antonio Banderas Jennifer Beals Madon...</td>\n",
              "      <td>[{'name': 'Allison Anders', 'gender': 1, 'depa...</td>\n",
              "      <td>Allison Anders</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>Star Wars</td>\n",
              "      <td>Adventure Action Science Fiction</td>\n",
              "      <td>en</td>\n",
              "      <td>11000000</td>\n",
              "      <td>126.393695</td>\n",
              "      <td>25-05-1977</td>\n",
              "      <td>775398007</td>\n",
              "      <td>121.0</td>\n",
              "      <td>8.1</td>\n",
              "      <td>...</td>\n",
              "      <td>http://www.starwars.com/films/star-wars-episod...</td>\n",
              "      <td>android galaxy hermit death star lightsaber</td>\n",
              "      <td>Princess Leia is captured and held hostage by ...</td>\n",
              "      <td>[{\"name\": \"Lucasfilm\", \"id\": 1}, {\"name\": \"Twe...</td>\n",
              "      <td>[{\"iso_3166_1\": \"US\", \"name\": \"United States o...</td>\n",
              "      <td>[{\"iso_639_1\": \"en\", \"name\": \"English\"}]</td>\n",
              "      <td>A long time ago in a galaxy far, far away...</td>\n",
              "      <td>Mark Hamill Harrison Ford Carrie Fisher Peter ...</td>\n",
              "      <td>[{'name': 'George Lucas', 'gender': 2, 'depart...</td>\n",
              "      <td>George Lucas</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>Finding Nemo</td>\n",
              "      <td>Animation Family</td>\n",
              "      <td>en</td>\n",
              "      <td>94000000</td>\n",
              "      <td>85.688789</td>\n",
              "      <td>30-05-2003</td>\n",
              "      <td>940335536</td>\n",
              "      <td>100.0</td>\n",
              "      <td>7.6</td>\n",
              "      <td>...</td>\n",
              "      <td>http://movies.disney.com/finding-nemo</td>\n",
              "      <td>father son relationship harbor underwater fish...</td>\n",
              "      <td>Nemo, an adventurous young clownfish, is unexp...</td>\n",
              "      <td>[{\"name\": \"Pixar Animation Studios\", \"id\": 3}]</td>\n",
              "      <td>[{\"iso_3166_1\": \"US\", \"name\": \"United States o...</td>\n",
              "      <td>[{\"iso_639_1\": \"en\", \"name\": \"English\"}]</td>\n",
              "      <td>There are 3.7 trillion fish in the ocean, they...</td>\n",
              "      <td>Albert Brooks Ellen DeGeneres Alexander Gould ...</td>\n",
              "      <td>[{'name': 'Andrew Stanton', 'gender': 2, 'depa...</td>\n",
              "      <td>Andrew Stanton</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>Forrest Gump</td>\n",
              "      <td>Comedy Drama Romance</td>\n",
              "      <td>en</td>\n",
              "      <td>55000000</td>\n",
              "      <td>138.133331</td>\n",
              "      <td>06-07-1994</td>\n",
              "      <td>677945399</td>\n",
              "      <td>142.0</td>\n",
              "      <td>8.2</td>\n",
              "      <td>...</td>\n",
              "      <td>NaN</td>\n",
              "      <td>vietnam veteran hippie mentally disabled runni...</td>\n",
              "      <td>A man with a low IQ has accomplished great thi...</td>\n",
              "      <td>[{\"name\": \"Paramount Pictures\", \"id\": 4}]</td>\n",
              "      <td>[{\"iso_3166_1\": \"US\", \"name\": \"United States o...</td>\n",
              "      <td>[{\"iso_639_1\": \"en\", \"name\": \"English\"}]</td>\n",
              "      <td>The world will never be the same, once you've ...</td>\n",
              "      <td>Tom Hanks Robin Wright Gary Sinise Mykelti Wil...</td>\n",
              "      <td>[{'name': 'Alan Silvestri', 'gender': 2, 'depa...</td>\n",
              "      <td>Robert Zemeckis</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>American Beauty</td>\n",
              "      <td>Drama</td>\n",
              "      <td>en</td>\n",
              "      <td>15000000</td>\n",
              "      <td>80.878605</td>\n",
              "      <td>15-09-1999</td>\n",
              "      <td>356296601</td>\n",
              "      <td>122.0</td>\n",
              "      <td>7.9</td>\n",
              "      <td>...</td>\n",
              "      <td>http://www.dreamworks.com/ab/</td>\n",
              "      <td>male nudity female nudity adultery midlife cri...</td>\n",
              "      <td>Lester Burnham, a depressed suburban father in...</td>\n",
              "      <td>[{\"name\": \"DreamWorks SKG\", \"id\": 27}, {\"name\"...</td>\n",
              "      <td>[{\"iso_3166_1\": \"US\", \"name\": \"United States o...</td>\n",
              "      <td>[{\"iso_639_1\": \"en\", \"name\": \"English\"}]</td>\n",
              "      <td>Look closer.</td>\n",
              "      <td>Kevin Spacey Annette Bening Thora Birch Wes Be...</td>\n",
              "      <td>[{'name': 'Thomas Newman', 'gender': 2, 'depar...</td>\n",
              "      <td>Sam Mendes</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>5 rows × 21 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-40e97399-3aa8-4657-88a3-ddfd07e1ac3f')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-40e97399-3aa8-4657-88a3-ddfd07e1ac3f button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-40e97399-3aa8-4657-88a3-ddfd07e1ac3f');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-19132fde-0591-403a-b98e-7e4a9f3525ce\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-19132fde-0591-403a-b98e-7e4a9f3525ce')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-19132fde-0591-403a-b98e-7e4a9f3525ce button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df"
            }
          },
          "metadata": {},
          "execution_count": 88
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hE4MZMhNKnHD",
        "outputId": "af3ecf68-87ae-442e-b419-3e3337c9603c"
      },
      "execution_count": 89,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 4760 entries, 0 to 4759\n",
            "Data columns (total 21 columns):\n",
            " #   Column                    Non-Null Count  Dtype  \n",
            "---  ------                    --------------  -----  \n",
            " 0   Movie_ID                  4760 non-null   int64  \n",
            " 1   Movie_Title               4760 non-null   object \n",
            " 2   Movie_Genre               4760 non-null   object \n",
            " 3   Movie_Language            4760 non-null   object \n",
            " 4   Movie_Budget              4760 non-null   int64  \n",
            " 5   Movie_Popularity          4760 non-null   float64\n",
            " 6   Movie_Release_Date        4760 non-null   object \n",
            " 7   Movie_Revenue             4760 non-null   int64  \n",
            " 8   Movie_Runtime             4758 non-null   float64\n",
            " 9   Movie_Vote                4760 non-null   float64\n",
            " 10  Movie_Vote_Count          4760 non-null   int64  \n",
            " 11  Movie_Homepage            1699 non-null   object \n",
            " 12  Movie_Keywords            4373 non-null   object \n",
            " 13  Movie_Overview            4757 non-null   object \n",
            " 14  Movie_Production_House    4760 non-null   object \n",
            " 15  Movie_Production_Country  4760 non-null   object \n",
            " 16  Movie_Spoken_Language     4760 non-null   object \n",
            " 17  Movie_Tagline             3942 non-null   object \n",
            " 18  Movie_Cast                4733 non-null   object \n",
            " 19  Movie_Crew                4760 non-null   object \n",
            " 20  Movie_Director            4738 non-null   object \n",
            "dtypes: float64(3), int64(4), object(14)\n",
            "memory usage: 781.1+ KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kVi6CB4sKuGT",
        "outputId": "15e2528d-7728-4b54-a563-a4f40394b414"
      },
      "execution_count": 90,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(4760, 21)"
            ]
          },
          "metadata": {},
          "execution_count": 90
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.columns"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hOuuCILkKy92",
        "outputId": "a2b77bc3-4fd5-4053-9f9e-cd056c2b72d7"
      },
      "execution_count": 91,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['Movie_ID', 'Movie_Title', 'Movie_Genre', 'Movie_Language',\n",
              "       'Movie_Budget', 'Movie_Popularity', 'Movie_Release_Date',\n",
              "       'Movie_Revenue', 'Movie_Runtime', 'Movie_Vote', 'Movie_Vote_Count',\n",
              "       'Movie_Homepage', 'Movie_Keywords', 'Movie_Overview',\n",
              "       'Movie_Production_House', 'Movie_Production_Country',\n",
              "       'Movie_Spoken_Language', 'Movie_Tagline', 'Movie_Cast', 'Movie_Crew',\n",
              "       'Movie_Director'],\n",
              "      dtype='object')"
            ]
          },
          "metadata": {},
          "execution_count": 91
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Get Feature Selection"
      ],
      "metadata": {
        "id": "U8BwPk0JTgTF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df_features = df[['Movie_Genre', 'Movie_Keywords', 'Movie_Tagline', 'Movie_Cast', 'Movie_Director']].fillna('')"
      ],
      "metadata": {
        "id": "OdClgr1OK2gh"
      },
      "execution_count": 92,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_features.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "T3tncm1CK9k4",
        "outputId": "ec1004ca-628b-4adf-9e31-45bf83ba2f95"
      },
      "execution_count": 93,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(4760, 5)"
            ]
          },
          "metadata": {},
          "execution_count": 93
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df_features"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "gJjdKDKJLHe6",
        "outputId": "d659ac02-3078-4f59-c2c0-8edb19caba44"
      },
      "execution_count": 94,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                           Movie_Genre  \\\n",
              "0                         Crime Comedy   \n",
              "1     Adventure Action Science Fiction   \n",
              "2                     Animation Family   \n",
              "3                 Comedy Drama Romance   \n",
              "4                                Drama   \n",
              "...                                ...   \n",
              "4755                            Horror   \n",
              "4756               Comedy Family Drama   \n",
              "4757                    Thriller Drama   \n",
              "4758                            Family   \n",
              "4759                       Documentary   \n",
              "\n",
              "                                         Movie_Keywords  \\\n",
              "0             hotel new year's eve witch bet hotel room   \n",
              "1           android galaxy hermit death star lightsaber   \n",
              "2     father son relationship harbor underwater fish...   \n",
              "3     vietnam veteran hippie mentally disabled runni...   \n",
              "4     male nudity female nudity adultery midlife cri...   \n",
              "...                                                 ...   \n",
              "4755                                                      \n",
              "4756                                                      \n",
              "4757                     christian film sex trafficking   \n",
              "4758                                                      \n",
              "4759  music actors legendary perfomer classic hollyw...   \n",
              "\n",
              "                                          Movie_Tagline  \\\n",
              "0     Twelve outrageous guests. Four scandalous requ...   \n",
              "1          A long time ago in a galaxy far, far away...   \n",
              "2     There are 3.7 trillion fish in the ocean, they...   \n",
              "3     The world will never be the same, once you've ...   \n",
              "4                                          Look closer.   \n",
              "...                                                 ...   \n",
              "4755                The hot spot where Satan's waitin'.   \n",
              "4756           It’s better to stand out than to fit in.   \n",
              "4757           She never knew it could happen to her...   \n",
              "4758                                                      \n",
              "4759                                                      \n",
              "\n",
              "                                             Movie_Cast     Movie_Director  \n",
              "0     Tim Roth Antonio Banderas Jennifer Beals Madon...     Allison Anders  \n",
              "1     Mark Hamill Harrison Ford Carrie Fisher Peter ...       George Lucas  \n",
              "2     Albert Brooks Ellen DeGeneres Alexander Gould ...     Andrew Stanton  \n",
              "3     Tom Hanks Robin Wright Gary Sinise Mykelti Wil...    Robert Zemeckis  \n",
              "4     Kevin Spacey Annette Bening Thora Birch Wes Be...         Sam Mendes  \n",
              "...                                                 ...                ...  \n",
              "4755  Lisa Hart Carroll Michael Des Barres Paul Drak...         Pece Dingo  \n",
              "4756  Roni Akurati Brighton Sharbino Jason Lee Anjul...       Frank Lotito  \n",
              "4757  Nicole Smolen Kim Baldwin Ariana Stephens Brys...       Jaco Booyens  \n",
              "4758                                                                        \n",
              "4759                                    Tony Oppedisano  Simon Napier-Bell  \n",
              "\n",
              "[4760 rows x 5 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-80878a0e-67bb-40d3-b3d4-67eea0018f98\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Movie_Genre</th>\n",
              "      <th>Movie_Keywords</th>\n",
              "      <th>Movie_Tagline</th>\n",
              "      <th>Movie_Cast</th>\n",
              "      <th>Movie_Director</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Crime Comedy</td>\n",
              "      <td>hotel new year's eve witch bet hotel room</td>\n",
              "      <td>Twelve outrageous guests. Four scandalous requ...</td>\n",
              "      <td>Tim Roth Antonio Banderas Jennifer Beals Madon...</td>\n",
              "      <td>Allison Anders</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Adventure Action Science Fiction</td>\n",
              "      <td>android galaxy hermit death star lightsaber</td>\n",
              "      <td>A long time ago in a galaxy far, far away...</td>\n",
              "      <td>Mark Hamill Harrison Ford Carrie Fisher Peter ...</td>\n",
              "      <td>George Lucas</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Animation Family</td>\n",
              "      <td>father son relationship harbor underwater fish...</td>\n",
              "      <td>There are 3.7 trillion fish in the ocean, they...</td>\n",
              "      <td>Albert Brooks Ellen DeGeneres Alexander Gould ...</td>\n",
              "      <td>Andrew Stanton</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Comedy Drama Romance</td>\n",
              "      <td>vietnam veteran hippie mentally disabled runni...</td>\n",
              "      <td>The world will never be the same, once you've ...</td>\n",
              "      <td>Tom Hanks Robin Wright Gary Sinise Mykelti Wil...</td>\n",
              "      <td>Robert Zemeckis</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Drama</td>\n",
              "      <td>male nudity female nudity adultery midlife cri...</td>\n",
              "      <td>Look closer.</td>\n",
              "      <td>Kevin Spacey Annette Bening Thora Birch Wes Be...</td>\n",
              "      <td>Sam Mendes</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4755</th>\n",
              "      <td>Horror</td>\n",
              "      <td></td>\n",
              "      <td>The hot spot where Satan's waitin'.</td>\n",
              "      <td>Lisa Hart Carroll Michael Des Barres Paul Drak...</td>\n",
              "      <td>Pece Dingo</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4756</th>\n",
              "      <td>Comedy Family Drama</td>\n",
              "      <td></td>\n",
              "      <td>It’s better to stand out than to fit in.</td>\n",
              "      <td>Roni Akurati Brighton Sharbino Jason Lee Anjul...</td>\n",
              "      <td>Frank Lotito</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4757</th>\n",
              "      <td>Thriller Drama</td>\n",
              "      <td>christian film sex trafficking</td>\n",
              "      <td>She never knew it could happen to her...</td>\n",
              "      <td>Nicole Smolen Kim Baldwin Ariana Stephens Brys...</td>\n",
              "      <td>Jaco Booyens</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4758</th>\n",
              "      <td>Family</td>\n",
              "      <td></td>\n",
              "      <td></td>\n",
              "      <td></td>\n",
              "      <td></td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4759</th>\n",
              "      <td>Documentary</td>\n",
              "      <td>music actors legendary perfomer classic hollyw...</td>\n",
              "      <td></td>\n",
              "      <td>Tony Oppedisano</td>\n",
              "      <td>Simon Napier-Bell</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>4760 rows × 5 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-80878a0e-67bb-40d3-b3d4-67eea0018f98')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-80878a0e-67bb-40d3-b3d4-67eea0018f98 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-80878a0e-67bb-40d3-b3d4-67eea0018f98');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-0299d335-e1ac-4b7f-b302-0c093e862bc3\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-0299d335-e1ac-4b7f-b302-0c093e862bc3')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-0299d335-e1ac-4b7f-b302-0c093e862bc3 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "  <div id=\"id_c7e7a6a8-fe61-4773-a369-dbc590df4013\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('df_features')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_c7e7a6a8-fe61-4773-a369-dbc590df4013 button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('df_features');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df_features",
              "summary": "{\n  \"name\": \"df_features\",\n  \"rows\": 4760,\n  \"fields\": [\n    {\n      \"column\": \"Movie_Genre\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 1164,\n        \"samples\": [\n          \"Family Animation Adventure\",\n          \"Adventure Science Fiction Action\",\n          \"Action Crime Drama Romance Thriller\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Movie_Keywords\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 4203,\n        \"samples\": [\n          \"canada nazis sequel spin off ancient evil\",\n          \"sex professor wedding woman director columbia university\",\n          \"prophecy sea beach gold small town\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Movie_Tagline\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 3928,\n        \"samples\": [\n          \"The messenger must be silenced.\",\n          \"It's not the house that's haunted.\",\n          \"The final hunt begins.\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Movie_Cast\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 4715,\n        \"samples\": [\n          \"Robin Tunney Fairuza Balk Neve Campbell Rachel True Skeet Ulrich\",\n          \"Peter Sellers Christopher Plummer Herbert Lom Catherine Schell Peter Arne\",\n          \"John Wayne Laraine Day Cedric Hardwicke Judith Anderson Anthony Quinn\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Movie_Director\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2332,\n        \"samples\": [\n          \"Rob McKittrick\",\n          \"Terron R. Parsons\",\n          \"Cyrus Nowrasteh\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 94
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "X = df_features['Movie_Genre'] + ' ' + df_features['Movie_Keywords'] + ' ' + df_features['Movie_Tagline'] + ' ' + df_features['Movie_Cast'] + ' ' + df_features['Movie_Director']"
      ],
      "metadata": {
        "id": "H5l8Wu4XLH_R"
      },
      "execution_count": 95,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        " X"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bu1TGcTWLITA",
        "outputId": "d79f5788-a751-45c7-db52-e889517b5610"
      },
      "execution_count": 96,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0       Crime Comedy hotel new year's eve witch bet ho...\n",
              "1       Adventure Action Science Fiction android galax...\n",
              "2       Animation Family father son relationship harbo...\n",
              "3       Comedy Drama Romance vietnam veteran hippie me...\n",
              "4       Drama male nudity female nudity adultery midli...\n",
              "                              ...                        \n",
              "4755    Horror  The hot spot where Satan's waitin'. Li...\n",
              "4756    Comedy Family Drama  It’s better to stand out ...\n",
              "4757    Thriller Drama christian film sex trafficking ...\n",
              "4758                                           Family    \n",
              "4759    Documentary music actors legendary perfomer cl...\n",
              "Length: 4760, dtype: object"
            ]
          },
          "metadata": {},
          "execution_count": 96
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "X.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gaUxwwI7LIU1",
        "outputId": "42e77aee-8629-4f16-c95a-b7471c321eb0"
      },
      "execution_count": 97,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(4760,)"
            ]
          },
          "metadata": {},
          "execution_count": 97
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Get feature Text Conversion to Tokens"
      ],
      "metadata": {
        "id": "YfbhYDmOUCWR"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.feature_extraction.text import TfidfVectorizer"
      ],
      "metadata": {
        "id": "Xv70zTYFLIje"
      },
      "execution_count": 98,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "tfidf = TfidfVectorizer()"
      ],
      "metadata": {
        "id": "xxebaCCuLtI3"
      },
      "execution_count": 99,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X = tfidf.fit_transform(X)"
      ],
      "metadata": {
        "id": "IkJAJ4dTLtRH"
      },
      "execution_count": 100,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ipen_nDOLtjv",
        "outputId": "ea9f7e0c-b4e3-457f-e5b2-df6f86f948cf"
      },
      "execution_count": 101,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(4760, 17258)"
            ]
          },
          "metadata": {},
          "execution_count": 101
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(X)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FnagOGAyMK9c",
        "outputId": "1257486f-3298-4660-b223-275944d543a1"
      },
      "execution_count": 102,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "  (0, 617)\t0.1633382144407513\n",
            "  (0, 492)\t0.1432591540388685\n",
            "  (0, 15413)\t0.1465525095337543\n",
            "  (0, 9675)\t0.14226057295252661\n",
            "  (0, 9465)\t0.1659841367820977\n",
            "  (0, 1390)\t0.16898383612799558\n",
            "  (0, 7825)\t0.09799561597509843\n",
            "  (0, 1214)\t0.13865857545144072\n",
            "  (0, 729)\t0.13415063359531618\n",
            "  (0, 13093)\t0.1432591540388685\n",
            "  (0, 15355)\t0.10477815972666779\n",
            "  (0, 9048)\t0.0866842116160778\n",
            "  (0, 11161)\t0.06250380151644369\n",
            "  (0, 16773)\t0.17654247479915475\n",
            "  (0, 5612)\t0.08603537588547631\n",
            "  (0, 16735)\t0.10690083751525419\n",
            "  (0, 7904)\t0.13348000542112332\n",
            "  (0, 15219)\t0.09800472886453934\n",
            "  (0, 11242)\t0.07277788238484746\n",
            "  (0, 3878)\t0.11998399582562203\n",
            "  (0, 5499)\t0.11454057510303811\n",
            "  (0, 7071)\t0.19822417598406614\n",
            "  (0, 7454)\t0.14745635785412262\n",
            "  (0, 1495)\t0.19712637387361423\n",
            "  (0, 9206)\t0.15186283580984414\n",
            "  :\t:\n",
            "  (4757, 5455)\t0.12491480594769522\n",
            "  (4757, 2967)\t0.16273475835631626\n",
            "  (4757, 8464)\t0.23522565554066333\n",
            "  (4757, 6938)\t0.17088173678136628\n",
            "  (4757, 8379)\t0.17480603856721913\n",
            "  (4757, 15303)\t0.07654356007668191\n",
            "  (4757, 15384)\t0.09754322497537371\n",
            "  (4757, 7649)\t0.11479421494340192\n",
            "  (4757, 10896)\t0.14546473055066447\n",
            "  (4757, 4494)\t0.05675298448720501\n",
            "  (4758, 5238)\t1.0\n",
            "  (4759, 11264)\t0.33947721804318337\n",
            "  (4759, 11708)\t0.33947721804318337\n",
            "  (4759, 205)\t0.3237911628497312\n",
            "  (4759, 8902)\t0.3040290704566037\n",
            "  (4759, 14062)\t0.3237911628497312\n",
            "  (4759, 3058)\t0.2812896191863103\n",
            "  (4759, 7130)\t0.26419662449963793\n",
            "  (4759, 10761)\t0.3126617295732147\n",
            "  (4759, 4358)\t0.18306542312175342\n",
            "  (4759, 14051)\t0.20084315377640435\n",
            "  (4759, 5690)\t0.19534291014627303\n",
            "  (4759, 15431)\t0.19628653185946862\n",
            "  (4759, 1490)\t0.21197258705292082\n",
            "  (4759, 10666)\t0.15888268987343043\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Get Similaarity Score using Cosine Similarity"
      ],
      "metadata": {
        "id": "0a1hwzaRUTCI"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics.pairwise import cosine_similarity"
      ],
      "metadata": {
        "id": "KAu7Bv1eMOri"
      },
      "execution_count": 103,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "Similarity_Score = cosine_similarity(X)"
      ],
      "metadata": {
        "id": "dBHA85QnMPC2"
      },
      "execution_count": 104,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "Similarity_Score"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WrzcBBVxMPK5",
        "outputId": "2db95303-9c83-4076-c3ab-da6dc8fca6fc"
      },
      "execution_count": 105,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([[1.        , 0.01351235, 0.03570468, ..., 0.        , 0.        ,\n",
              "        0.        ],\n",
              "       [0.01351235, 1.        , 0.00806674, ..., 0.        , 0.        ,\n",
              "        0.        ],\n",
              "       [0.03570468, 0.00806674, 1.        , ..., 0.        , 0.08014876,\n",
              "        0.        ],\n",
              "       ...,\n",
              "       [0.        , 0.        , 0.        , ..., 1.        , 0.        ,\n",
              "        0.        ],\n",
              "       [0.        , 0.        , 0.08014876, ..., 0.        , 1.        ,\n",
              "        0.        ],\n",
              "       [0.        , 0.        , 0.        , ..., 0.        , 0.        ,\n",
              "        1.        ]])"
            ]
          },
          "metadata": {},
          "execution_count": 105
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "Similarity_Score.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GHsZkSWPMPVi",
        "outputId": "a96ad33b-ea91-4626-b936-62e253578635"
      },
      "execution_count": 106,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(4760, 4760)"
            ]
          },
          "metadata": {},
          "execution_count": 106
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Get Movie Name as Input from User and Validate for Closest Spelling"
      ],
      "metadata": {
        "id": "RzUNlK2IUncS"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "Favourite_Movie_Name = input('  Enter your Favourite Movie Name: ')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Os2Q4K4CMPir",
        "outputId": "8ff5b1f0-9340-4183-9c4a-fd5ceed96b8a"
      },
      "execution_count": 107,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "  Enter your Favourite Movie Name: Avataar\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "All_Movies_Title_List = df['Movie_Title'].tolist()"
      ],
      "metadata": {
        "id": "sz2-RiqvQGL4"
      },
      "execution_count": 108,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import difflib"
      ],
      "metadata": {
        "id": "S0yWcotrQGTk"
      },
      "execution_count": 109,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "Movie_Recommendation = difflib.get_close_matches(Favourite_Movie_Name, All_Movies_Title_List)\n",
        "print(Movie_Recommendation)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9otTqSRAQGaG",
        "outputId": "f9508c1e-6570-4132-c9b0-ae0cab35e0fa"
      },
      "execution_count": 110,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Avatar', 'Anastasia']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "Close_Match = Movie_Recommendation[0]\n",
        "print(Close_Match)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GZPibEFpQGj1",
        "outputId": "1c214cc9-1e47-4517-c4ea-bb317fd4e90d"
      },
      "execution_count": 111,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Avatar\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "Index_of_Close_Match_Movie = df[df.Movie_Title == Close_Match]['Movie_ID'].values[0]\n",
        "print(Index_of_Close_Match_Movie)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GYp2ce7GQqMy",
        "outputId": "c01c38f9-03bc-4dfc-a7d5-9f37aa863023"
      },
      "execution_count": 112,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2692\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "Recommendation_Score = list(enumerate(Similarity_Score[Index_of_Close_Match_Movie]))\n",
        "print(Recommendation_Score)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jU1vj8CvQyL8",
        "outputId": "ce1246b0-325f-4534-a8fa-b2685b3201ea"
      },
      "execution_count": 113,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[(0, 0.009805093506053453), (1, 0.0), (2, 0.0), (3, 0.00800429043895183), (4, 0.0026759665928032302), (5, 0.009639835665946627), (6, 0.0049636657561850026), (7, 0.012848827437220958), (8, 0.0027543335470164663), (9, 0.00607882290416431), (10, 0.007539724639541887), (11, 0.0026263170118314906), (12, 0.002708340354961457), (13, 0.012904730427356216), (14, 0.0), (15, 0.022556564866386044), (16, 0.005959078936688496), (17, 0.0), (18, 0.013639824714195078), (19, 0.008784739948684396), (20, 0.0026527570934446066), (21, 0.015211614027840471), (22, 0.006522322352622825), (23, 0.0026429172195160193), (24, 0.0016564482636435309), (25, 0.025600660315408176), (26, 0.0024815199490618002), (27, 0.0047922703978129), (28, 0.0), (29, 0.023288277583204436), (30, 0.004648836119227042), (31, 0.006723965537835127), (32, 0.007984548069367697), (33, 0.018612326068635436), (34, 0.007439622267479848), (35, 0.0060612328203774185), (36, 0.0), (37, 0.0), (38, 0.008085428274959462), (39, 0.0046323263203813065), (40, 0.015305064222782005), (41, 0.0028220612513682524), (42, 0.007236825272071698), (43, 0.014851289474516489), (44, 0.03961780430399104), (45, 0.08999324643162435), (46, 0.01855499596172605), (47, 0.010374759033888029), (48, 0.015673410180680997), (49, 0.0), (50, 0.006986992676753986), (51, 0.014965979411782002), (52, 0.013600804094978335), (53, 0.0), (54, 0.0), (55, 0.0), (56, 0.006687995450791239), (57, 0.010835008478228547), (58, 0.0), (59, 0.0), (60, 0.007788672977779784), (61, 0.017658795452635247), (62, 0.10153560702418994), (63, 0.00724637379048299), (64, 0.0), (65, 0.031680929113056686), (66, 0.0025312341363153924), (67, 0.04506617878405939), (68, 0.022589410734540884), (69, 0.00506551508596364), (70, 0.012784303893544423), (71, 0.002598233031967091), (72, 0.011335815706635272), (73, 0.0), (74, 0.002697321222497816), (75, 0.012892746449532828), (76, 0.0037642771162936252), (77, 0.003476980872095499), (78, 0.009399606571884909), (79, 0.009076618790839581), (80, 0.004227109798982706), (81, 0.007009943535800456), (82, 0.011894144332662657), (83, 0.018501078945740605), (84, 0.0618237599684129), (85, 0.015565415762667165), (86, 0.011733847489721559), (87, 0.013731711116033066), (88, 0.022301178722772527), (89, 0.04014807769109404), (90, 0.004511298820312949), (91, 0.0), (92, 0.002231938202318901), (93, 0.004418656840322172), (94, 0.004236585948952706), (95, 0.004745609331166691), (96, 0.008895438584707134), (97, 0.002225672039651193), (98, 0.00248340938176191), (99, 0.01010872536394476), (100, 0.0), (101, 0.0), (102, 0.0050401893607578485), (103, 0.002196696924815654), (104, 0.00916249023695782), (105, 0.009532098755129267), (106, 0.017511756601740806), (107, 0.00810878589263473), (108, 0.03871190052571693), (109, 0.038488255428289986), (110, 0.08361784775029485), (111, 0.00892830755196627), (112, 0.028472602360715568), (113, 0.007487310843562389), (114, 0.002538593432573124), (115, 0.002593300200593264), (116, 0.02423134884513523), (117, 0.0), (118, 0.0047336369622742935), (119, 0.008932839836200659), (120, 0.009912331765059942), (121, 0.0023309647694089563), (122, 0.006517403480064114), (123, 0.018256088885426403), (124, 0.024984856011144883), (125, 0.012801531158627047), (126, 0.03803411394029396), (127, 0.0024694587388694603), (128, 0.005117957196142506), (129, 0.0017710145837505121), (130, 0.011926867676679177), (131, 0.006655142039509908), (132, 0.0022485035909542398), (133, 0.0), (134, 0.0), (135, 0.004609422560900165), (136, 0.002342053663543897), (137, 0.052487743978234754), (138, 0.032196594696629596), (139, 0.00793805341964405), (140, 0.0023757143815839364), (141, 0.0), (142, 0.01924033807026037), (143, 0.0074218727251426225), (144, 0.017350164505517556), (145, 0.019128060100674707), (146, 0.0), (147, 0.01798970888682872), (148, 0.010606847740924956), (149, 0.011746502833415905), (150, 0.0), (151, 0.0), (152, 0.004480162377431886), (153, 0.0), (154, 0.002380610004741567), (155, 0.023537765450918877), (156, 0.007396517906534802), (157, 0.002415439486141447), (158, 0.002274967685727569), (159, 0.007126037020866246), (160, 0.018298437262288456), (161, 0.04350231968158566), (162, 0.007770799696963449), (163, 0.0), (164, 0.0086637829941784), (165, 0.002192430843204887), (166, 0.03236744328857419), (167, 0.026576509643169363), (168, 0.005162629015437511), (169, 0.002491783750451106), (170, 0.010590419372720969), (171, 0.0), (172, 0.041690425384126525), (173, 0.01695754465504918), (174, 0.030569480499441422), (175, 0.023330531483932517), (176, 0.027183803724459624), (177, 0.005599808753936733), (178, 0.002667965049488923), (179, 0.030707903325990372), (180, 0.007560424083753987), (181, 0.014055923457905324), (182, 0.009177613098031678), (183, 0.008350342502147893), (184, 0.0022333195719391554), (185, 0.03981648215324947), (186, 0.0), (187, 0.004046624716605281), (188, 0.0), (189, 0.004777355844485406), (190, 0.012138750265674795), (191, 0.00411617790201361), (192, 0.0027430559563033185), (193, 0.029212491040047014), (194, 0.002034839745506438), (195, 0.0021317422811621754), (196, 0.002130241788619929), (197, 0.00859704253241558), (198, 0.002573256321933336), (199, 0.018959792932713843), (200, 0.006317406038489515), (201, 0.012194922563079247), (202, 0.0016641723699352556), (203, 0.01692391575379628), (204, 0.018686269670332167), (205, 0.0), (206, 0.010195436607244203), (207, 0.013202287890523336), (208, 0.014564317291621241), (209, 0.016326637209159098), (210, 0.038872494075225), (211, 0.0026509436265181466), (212, 0.01673880855230024), (213, 0.049335863613711506), (214, 0.0), (215, 0.002491610501274281), (216, 0.009964319549763758), (217, 0.006895954353204596), (218, 0.016329345660994338), (219, 0.0), (220, 0.004877383327231498), (221, 0.002411361490287575), (222, 0.017856013028360415), (223, 0.0), (224, 0.007353548211987467), (225, 0.0), (226, 0.0025358335946023417), (227, 0.049272711641777656), (228, 0.0019207863172057056), (229, 0.002364464894441411), (230, 0.00639704758425901), (231, 0.013776482994224605), (232, 0.007072494943779912), (233, 0.004553254985288596), (234, 0.003970509617032526), (235, 0.0028626037655011655), (236, 0.013361417399169878), (237, 0.0), (238, 0.007292058096564207), (239, 0.004893411026998544), (240, 0.02640964525511218), (241, 0.02846230566947309), (242, 0.007883152373824122), (243, 0.009658171853199466), (244, 0.011434438545935371), (245, 0.0), (246, 0.002697163563809614), (247, 0.002507649315273456), (248, 0.006076898456420151), (249, 0.0022242181571218047), (250, 0.029605156266211453), (251, 0.013867966455367267), (252, 0.013883632146620802), (253, 0.0027728619056607952), (254, 0.06351452702158421), (255, 0.007486787644460759), (256, 0.007180422705514563), (257, 0.021804620814370096), (258, 0.0), (259, 0.0), (260, 0.004375759434559263), (261, 0.02232369294417245), (262, 0.0026643359555147046), (263, 0.006216251561942655), (264, 0.0), (265, 0.0), (266, 0.010555380119079246), (267, 0.0021492676003019005), (268, 0.0022620244651643815), (269, 0.024722211015322175), (270, 0.010051806221174025), (271, 0.010513499130038398), (272, 0.0), (273, 0.010851325289581416), (274, 0.011035641459288753), (275, 0.0), (276, 0.013412243036761688), (277, 0.04305955678902839), (278, 0.0021843202599993133), (279, 0.01674439634537899), (280, 0.016137762281668154), (281, 0.010850110374057989), (282, 0.05879285017883316), (283, 0.006663066484764481), (284, 0.027210766517313724), (285, 0.008704678727235576), (286, 0.0021763451606793822), (287, 0.015182057023698533), (288, 0.009496377944736414), (289, 0.003702706209227987), (290, 0.0037646025269972177), (291, 0.010654114070260626), (292, 0.05110461872364794), (293, 0.0018032932320903585), (294, 0.0036732829549063557), (295, 0.0037622811700992434), (296, 0.015204844606541184), (297, 0.0), (298, 0.0), (299, 0.0), (300, 0.006258139455269685), (301, 0.0069485776645648555), (302, 0.0), (303, 0.0050061679094136795), (304, 0.010776123342338816), (305, 0.004608912986979318), (306, 0.004250577618359522), (307, 0.008540452172185265), (308, 0.002836039428752784), (309, 0.007241873038964715), (310, 0.0044324607065052745), (311, 0.006640720103355573), (312, 0.0), (313, 0.011588694147227201), (314, 0.00386727864603967), (315, 0.0046275791609617966), (316, 0.004275668536878031), (317, 0.01372437577101817), (318, 0.0027716213992394355), (319, 0.0), (320, 0.004836468342738552), (321, 0.010853546219663456), (322, 0.011011274215599966), (323, 0.004126702166598835), (324, 0.0023375564513999506), (325, 0.002396607136979531), (326, 0.003105938774714085), (327, 0.010031091446491825), (328, 0.043787258882396256), (329, 0.019680187212331626), (330, 0.01990757698892509), (331, 0.0), (332, 0.013291392972049707), (333, 0.010396647172797039), (334, 0.033097160057045466), (335, 0.0), (336, 0.0047110789913987), (337, 0.0), (338, 0.0), (339, 0.0), (340, 0.0070577890082476336), (341, 0.012040276910772649), (342, 0.017625924860547256), (343, 0.015792700017701194), (344, 0.0), (345, 0.024810895755894055), (346, 0.00904732990567095), (347, 0.004629011445466316), (348, 0.0025106049309844727), (349, 0.0024597751017132285), (350, 0.007783455522120415), (351, 0.001934949810470641), (352, 0.0), (353, 0.009247286364833024), (354, 0.01023318036745526), (355, 0.002338600461277963), (356, 0.01308537921357196), (357, 0.0021885661052920605), (358, 0.01524391279622352), (359, 0.0023274681266520665), (360, 0.04140490881144238), (361, 0.0), (362, 0.0), (363, 0.007177918653319793), (364, 0.018118667495208754), (365, 0.0), (366, 0.0), (367, 0.006777740856868494), (368, 0.00849246998822155), (369, 0.0054147171174585024), (370, 0.014201587388961134), (371, 0.028251554740421535), (372, 0.0023630726175345187), (373, 0.0024035937816996485), (374, 0.015464220140309494), (375, 0.004559317565774011), (376, 0.0), (377, 0.002613134236024629), (378, 0.002547043242925245), (379, 0.0), (380, 0.0052998836952428295), (381, 0.02609320340969504), (382, 0.0), (383, 0.019467817150654654), (384, 0.048561612573761986), (385, 0.007832134714130213), (386, 0.006839997396687533), (387, 0.032522091160063736), (388, 0.0023942044323020653), (389, 0.0045928926555422215), (390, 0.0), (391, 0.0), (392, 0.0), (393, 0.0), (394, 0.0), (395, 0.00272106521247246), (396, 0.009236073372609652), (397, 0.004218130295350773), (398, 0.02199549736073778), (399, 0.0023500375059201137), (400, 0.00251289546460505), (401, 0.0), (402, 0.011099556911853728), (403, 0.007717320665807713), (404, 0.0), (405, 0.0), (406, 0.013996421309263717), (407, 0.012576162839507807), (408, 0.04269519176334115), (409, 0.017054864370849368), (410, 0.0023595146802160606), (411, 0.0), (412, 0.04506044778254056), (413, 0.007014363525749394), (414, 0.00493284652771533), (415, 0.0), (416, 0.002324088327746965), (417, 0.010857053144102818), (418, 0.012363494963790644), (419, 0.0028564076731825015), (420, 0.004960790573790974), (421, 0.02749177219642947), (422, 0.006684770214378324), (423, 0.0), (424, 0.05839654732699123), (425, 0.005233653978455374), (426, 0.004315083525299143), (427, 0.0), (428, 0.027941476362352217), (429, 0.014907793983901895), (430, 0.028474447896110415), (431, 0.0029909808972183064), (432, 0.002157573346153142), (433, 0.016594829303328437), (434, 0.00909271578475179), (435, 0.009477836158719864), (436, 0.007999143568905942), (437, 0.014872318949017253), (438, 0.04307224044369871), (439, 0.0), (440, 0.0), (441, 0.007524058999258837), (442, 0.021288297567688543), (443, 0.00826944426866319), (444, 0.002825858774682473), (445, 0.007794521839692808), (446, 0.00888200665157438), (447, 0.01477043861892446), (448, 0.0029273791170721856), (449, 0.00823467413153059), (450, 0.015608519656568696), (451, 0.004633317948990186), (452, 0.011805040282430304), (453, 0.0019393347333000763), (454, 0.0), (455, 0.04213396440391408), (456, 0.002687049016489072), (457, 0.002327732812904547), (458, 0.015871922723417135), (459, 0.026041390263338297), (460, 0.004591946474043866), (461, 0.008378393185575846), (462, 0.03225758483924034), (463, 0.019270774055312006), (464, 0.008999856286562488), (465, 0.02832340194230098), (466, 0.002507384990996102), (467, 0.0045476787092075905), (468, 0.010463913523735657), (469, 0.0038125681688557884), (470, 0.014468577429467194), (471, 0.002368427181806095), (472, 0.00937363469527576), (473, 0.0022945038896853643), (474, 0.007434113526945559), (475, 0.003183017020864471), (476, 0.0027839829553150115), (477, 0.005239784974437232), (478, 0.0028703090546665397), (479, 0.04998855981862962), (480, 0.0022254937857947676), (481, 0.015469390328392467), (482, 0.014318865406517198), (483, 0.010147870988533602), (484, 0.0), (485, 0.010299890463609936), (486, 0.0), (487, 0.0024278315922302163), (488, 0.002453124966462652), (489, 0.003033907649847658), (490, 0.0025114046023391725), (491, 0.0), (492, 0.0), (493, 0.007590992590773915), (494, 0.007107534761405225), (495, 0.0022431563403783133), (496, 0.013381535196328247), (497, 0.00629601813997159), (498, 0.0), (499, 0.002760042990982669), (500, 0.01139692902865105), (501, 0.010495925548300913), (502, 0.014891603243137274), (503, 0.006882371442124131), (504, 0.002551508415229109), (505, 0.002409323202911005), (506, 0.0), (507, 0.0023814032611240723), (508, 0.0029161753848960135), (509, 0.00733202705436811), (510, 0.014297192125796505), (511, 0.016166552419491664), (512, 0.005483270579141841), (513, 0.005015028264463551), (514, 0.005003024616850094), (515, 0.022499833096115873), (516, 0.0), (517, 0.0), (518, 0.0029732402429394856), (519, 0.04913582561387614), (520, 0.0), (521, 0.006324471633262136), (522, 0.026704190546478417), (523, 0.01175475224186366), (524, 0.002326628494390853), (525, 0.0), (526, 0.0031892059612266465), (527, 0.012408426657113936), (528, 0.0), (529, 0.0), (530, 0.02974102103303271), (531, 0.0), (532, 0.010853692109028056), (533, 0.015999131525746606), (534, 0.01404914416124758), (535, 0.0), (536, 0.0), (537, 0.012728576163409102), (538, 0.010837176004175735), (539, 0.006923300446519886), (540, 0.03445972856479224), (541, 0.0024531262551875303), (542, 0.009974966884476081), (543, 0.01481514022208621), (544, 0.009753397860988314), (545, 0.013484509510887666), (546, 0.0), (547, 0.03205811100816747), (548, 0.0), (549, 0.0), (550, 0.005095713449789213), (551, 0.016277960178301926), (552, 0.0), (553, 0.018685764365025583), (554, 0.0), (555, 0.010805867563405055), (556, 0.0), (557, 0.0), (558, 0.008862695499612721), (559, 0.004110087166529763), (560, 0.011723796536706639), (561, 0.004843879649288874), (562, 0.005424022281125922), (563, 0.006446918984242734), (564, 0.002657027849458249), (565, 0.0), (566, 0.019085435302379772), (567, 0.0), (568, 0.0060923938011236784), (569, 0.0), (570, 0.0), (571, 0.00551243089187356), (572, 0.0), (573, 0.0), (574, 0.0), (575, 0.0), (576, 0.002858999118369583), (577, 0.0), (578, 0.03327816265992636), (579, 0.002570927431235828), (580, 0.007471013806577874), (581, 0.0064429088076600515), (582, 0.007738614071243571), (583, 0.005955003048448513), (584, 0.014718536886619442), (585, 0.0), (586, 0.015989792128490082), (587, 0.002789246217675594), (588, 0.0026354138296516643), (589, 0.0023504596104199846), (590, 0.06275727122098754), (591, 0.0), (592, 0.0), (593, 0.0269834518549629), (594, 0.0022668822325154735), (595, 0.005073766918951453), (596, 0.002841667503161745), (597, 0.008184692697223068), (598, 0.002363017019179979), (599, 0.0), (600, 0.006911988221385433), (601, 0.0), (602, 0.0), (603, 0.0), (604, 0.013082263186631318), (605, 0.0022316315763223366), (606, 0.00738281553042624), (607, 0.00195429012036482), (608, 0.006480886036499979), (609, 0.012436169884984381), (610, 0.0), (611, 0.00407474121950208), (612, 0.0026927305201672825), (613, 0.02210391733671185), (614, 0.00290989792253315), (615, 0.043627287472934005), (616, 0.007587604885805269), (617, 0.006036313815003582), (618, 0.029763727969072954), (619, 0.004592008813534647), (620, 0.015054170784840127), (621, 0.0098894425959586), (622, 0.015114877441477752), (623, 0.0026936257054534724), (624, 0.0023197786136598814), (625, 0.0039700919528630274), (626, 0.0021492988165263674), (627, 0.0034341999825618446), (628, 0.08334515876919323), (629, 0.0290204466032395), (630, 0.0), (631, 0.009361669401453363), (632, 0.03852152259053765), (633, 0.0045195689450570255), (634, 0.004532017668175815), (635, 0.012208498691708229), (636, 0.007220498423054623), (637, 0.044214370060605246), (638, 0.01648509407336536), (639, 0.003895629946806929), (640, 0.003862120234585781), (641, 0.022162243129839825), (642, 0.00617554124475728), (643, 0.02014941724072286), (644, 0.006791787033115819), (645, 0.0020714050466539096), (646, 0.0024389251045113143), (647, 0.002225248093371474), (648, 0.012277887423853677), (649, 0.0), (650, 0.0), (651, 0.008790443518269624), (652, 0.01454961180007468), (653, 0.012376187134664488), (654, 0.012319247296879221), (655, 0.0023683578516378546), (656, 0.0), (657, 0.02453562880347747), (658, 0.0), (659, 0.0023624315239011303), (660, 0.007468299121380835), (661, 0.004327776691481764), (662, 0.0), (663, 0.0), (664, 0.012230253012714354), (665, 0.0), (666, 0.005191363840721598), (667, 0.012288709705708509), (668, 0.009247180014652573), (669, 0.01913232163764439), (670, 0.027728288572825423), (671, 0.0067828701196653), (672, 0.021739478274217176), (673, 0.04277602512082654), (674, 0.0), (675, 0.06176991517572303), (676, 0.013790445822426273), (677, 0.01682247009934885), (678, 0.01274236717803005), (679, 0.0), (680, 0.0026971854142241744), (681, 0.0), (682, 0.043040904339148985), (683, 0.010850382331213299), (684, 0.01187270882417908), (685, 0.004739140064506008), (686, 0.0), (687, 0.00511838964431733), (688, 0.007920082561582203), (689, 0.01823124484931015), (690, 0.004292327916105059), (691, 0.022330801569338962), (692, 0.01577967045091189), (693, 0.028339830117329528), (694, 0.035178367818131856), (695, 0.010765812704594108), (696, 0.007196443040031081), (697, 0.009143071449328686), (698, 0.002399544762154424), (699, 0.0), (700, 0.0), (701, 0.015878620948365185), (702, 0.0), (703, 0.002252830558764676), (704, 0.0), (705, 0.008060671056134337), (706, 0.02288398192631816), (707, 0.002133185976689703), (708, 0.0), (709, 0.0), (710, 0.03578166731017038), (711, 0.0), (712, 0.0022406993971376544), (713, 0.0), (714, 0.0), (715, 0.010047304304865666), (716, 0.00749730430513755), (717, 0.0026448136161407753), (718, 0.0), (719, 0.011021069857465697), (720, 0.0), (721, 0.03336245332783653), (722, 0.0022788621644894975), (723, 0.003905451704110582), (724, 0.0), (725, 0.0), (726, 0.0), (727, 0.007024317991323226), (728, 0.007711282099805773), (729, 0.007972578233613352), (730, 0.0), (731, 0.002426041885645131), (732, 0.01224641375041674), (733, 0.01230753482660447), (734, 0.008527107655238415), (735, 0.003463159634339838), (736, 0.0), (737, 0.01026948217402053), (738, 0.00380050542824053), (739, 0.002894012255446743), (740, 0.0017013738490800241), (741, 0.0), (742, 0.012895262349341564), (743, 0.007346838592574463), (744, 0.0066118215152692235), (745, 0.006541447895988961), (746, 0.0), (747, 0.0), (748, 0.0069703375048933616), (749, 0.002537705888891391), (750, 0.007283807541207738), (751, 0.0), (752, 0.006874003656088703), (753, 0.013549278832237003), (754, 0.0), (755, 0.0024647317404651358), (756, 0.0040510836090402675), (757, 0.018171478905814088), (758, 0.006619783688263925), (759, 0.002309117906857392), (760, 0.013408755868769412), (761, 0.050844325355354554), (762, 0.015386234332469932), (763, 0.02069291081637438), (764, 0.0), (765, 0.004875714723265432), (766, 0.02863597006015581), (767, 0.002405830891505593), (768, 0.01889780127429161), (769, 0.0070559764342692744), (770, 0.0), (771, 0.0), (772, 0.0), (773, 0.0), (774, 0.03653446982082753), (775, 0.013580167832495795), (776, 0.016907533747342923), (777, 0.003048206537715965), (778, 0.006760120126778052), (779, 0.019778519028090427), (780, 0.0), (781, 0.0), (782, 0.008737001055913084), (783, 0.002671657768184265), (784, 0.0), (785, 0.0), (786, 0.0), (787, 0.030234382676036564), (788, 0.036775782506030336), (789, 0.0), (790, 0.011328819098868296), (791, 0.0027245490827624776), (792, 0.010223739969146536), (793, 0.0047911708785747225), (794, 0.016938690601848962), (795, 0.016724564291810132), (796, 0.01748508210449308), (797, 0.0), (798, 0.002420279154987218), (799, 0.013866844082999446), (800, 0.012330546240660194), (801, 0.010706865530756116), (802, 0.00504790855259478), (803, 0.004123319018849689), (804, 0.006430481765266979), (805, 0.0023452728300887567), (806, 0.009918568722061226), (807, 0.0), (808, 0.01788485830207994), (809, 0.011480022502538125), (810, 0.00431024470610246), (811, 0.004677175365825214), (812, 0.03134464238097974), (813, 0.0028484923414636154), (814, 0.013495540125448381), (815, 0.002265810207528326), (816, 0.007822688625960025), (817, 0.008811076124523943), (818, 0.03439755809850987), (819, 0.0), (820, 0.0), (821, 0.0060159760666970525), (822, 0.0), (823, 0.03170971693957012), (824, 0.02455387204481398), (825, 0.011336234973378517), (826, 0.002704815148187846), (827, 0.011088505143461765), (828, 0.009079231893502364), (829, 0.013067152965588674), (830, 0.03447452468561071), (831, 0.00504729347668347), (832, 0.02610503660845372), (833, 0.012768979339293338), (834, 0.006515346842433373), (835, 0.006210819751878022), (836, 0.028164079074357654), (837, 0.0), (838, 0.00846638251021233), (839, 0.0), (840, 0.0), (841, 0.0), (842, 0.014292048885850284), (843, 0.007487678947366412), (844, 0.012547501024285897), (845, 0.0074849403670845475), (846, 0.0), (847, 0.01044101072550268), (848, 0.002557744428375922), (849, 0.0046103472537448245), (850, 0.009269227266584062), (851, 0.008419793419722108), (852, 0.026315624754250793), (853, 0.01607702326648414), (854, 0.0024204130433707048), (855, 0.005267649046133167), (856, 0.002263834787264893), (857, 0.0028006579787448836), (858, 0.01786248303974472), (859, 0.0), (860, 0.016481212100768684), (861, 0.006156676188760678), (862, 0.006163646870521245), (863, 0.0065353030348067245), (864, 0.031860195855372704), (865, 0.0026041473034027975), (866, 0.013223819809213744), (867, 0.015447275691157163), (868, 0.0066380990252306385), (869, 0.007254016902358079), (870, 0.020332227193004895), (871, 0.002605879108742159), (872, 0.0027151279537172817), (873, 0.05064812913191185), (874, 0.03549031987804057), (875, 0.012828620175361183), (876, 0.016236183953495645), (877, 0.0512230973907653), (878, 0.013435345188327827), (879, 0.014840329123637929), (880, 0.007046905349603812), (881, 0.0), (882, 0.0), (883, 0.002422689099820759), (884, 0.0026386594931607945), (885, 0.02372906869332012), (886, 0.002377685816062925), (887, 0.0027576749224545974), (888, 0.015765180129318643), (889, 0.003263982140942741), (890, 0.0026450709873933557), (891, 0.004859604317280072), (892, 0.0), (893, 0.004160011744378803), (894, 0.009520951455559387), (895, 0.014602672301442823), (896, 0.015539368002936158), (897, 0.009174254862381888), (898, 0.004155926036290059), (899, 0.01444837727674443), (900, 0.01282649488429427), (901, 0.0021006570803087372), (902, 0.004732429780589892), (903, 0.0272937967913948), (904, 0.045049265599229504), (905, 0.013521019557386164), (906, 0.013082769368796992), (907, 0.002332300601765917), (908, 0.007227807872197648), (909, 0.0), (910, 0.006544699287657487), (911, 0.03585824955577745), (912, 0.0), (913, 0.0), (914, 0.0), (915, 0.011247273022572186), (916, 0.016917139639294917), (917, 0.021822162443509208), (918, 0.012096049309795825), (919, 0.004688274887806511), (920, 0.0), (921, 0.008473884306744563), (922, 0.00284543190818928), (923, 0.0068851967951298505), (924, 0.007930889582430515), (925, 0.002916183387409237), (926, 0.0), (927, 0.004525247754470468), (928, 0.012197504397565779), (929, 0.015192476876984534), (930, 0.007588642360831522), (931, 0.011680378019562551), (932, 0.0041240318599223), (933, 0.0025901424197287393), (934, 0.014284810246050515), (935, 0.0320740971372626), (936, 0.012343388786512692), (937, 0.01661899895760169), (938, 0.0), (939, 0.00906544737876302), (940, 0.006372201502734289), (941, 0.0023753858347316313), (942, 0.02404326236955836), (943, 0.0), (944, 0.002362909437140335), (945, 0.0), (946, 0.0), (947, 0.01918803569573748), (948, 0.008908360175058827), (949, 0.01083005059414121), (950, 0.0), (951, 0.002141013818313958), (952, 0.029031084004495476), (953, 0.005756518916356405), (954, 0.0), (955, 0.0), (956, 0.0), (957, 0.014312073755375083), (958, 0.006004028909589244), (959, 0.0024634028936061187), (960, 0.0), (961, 0.0), (962, 0.008633517179123244), (963, 0.01282335978690511), (964, 0.0), (965, 0.0), (966, 0.008596738901221878), (967, 0.02484089246980712), (968, 0.018377219999664365), (969, 0.002588635847946133), (970, 0.009447726677397602), (971, 0.0), (972, 0.0), (973, 0.0024986829749220254), (974, 0.00431872120142841), (975, 0.002374254485406639), (976, 0.028498609827027066), (977, 0.0), (978, 0.0), (979, 0.009887972165231157), (980, 0.0073892674550401615), (981, 0.006436594763438926), (982, 0.0), (983, 0.0), (984, 0.0024124304913493468), (985, 0.002901203439820041), (986, 0.014213770613722879), (987, 0.002630563204847358), (988, 0.014128718827695012), (989, 0.013990992406489752), (990, 0.0), (991, 0.007674540016661659), (992, 0.004935502243441057), (993, 0.002554833899416498), (994, 0.009767338355605823), (995, 0.0), (996, 0.00650992907297042), (997, 0.004149127110904068), (998, 0.002875096610449085), (999, 0.0028727435442566034), (1000, 0.012794194783292075), (1001, 0.0068140912017435416), (1002, 0.0024164625079969525), (1003, 0.02040558863047458), (1004, 0.0022732257076968914), (1005, 0.01236719175457826), (1006, 0.00951241049788545), (1007, 0.0026699680308093048), (1008, 0.0), (1009, 0.012169952798027534), (1010, 0.0), (1011, 0.0), (1012, 0.011077486485627775), (1013, 0.0), (1014, 0.007610412264289004), (1015, 0.022477148208897783), (1016, 0.0), (1017, 0.020210828878643068), (1018, 0.015920831393077692), (1019, 0.011046732439510036), (1020, 0.008735245570264399), (1021, 0.05671999964768967), (1022, 0.0), (1023, 0.04614573925419343), (1024, 0.037086309751285476), (1025, 0.0), (1026, 0.0024886894329191793), (1027, 0.002425178530119394), (1028, 0.0), (1029, 0.0), (1030, 0.050582789674035046), (1031, 0.0), (1032, 0.002395440149663579), (1033, 0.02132016719433776), (1034, 0.0024287885484453667), (1035, 0.01381887453098141), (1036, 0.002391995314691645), (1037, 0.007406593398245866), (1038, 0.0), (1039, 0.0), (1040, 0.0019808664673990114), (1041, 0.006711122649795384), (1042, 0.0021181778347175257), (1043, 0.03019341492590413), (1044, 0.006925941771792754), (1045, 0.01574002225933099), (1046, 0.028771864585929827), (1047, 0.012178017913835978), (1048, 0.009461601719983486), (1049, 0.0030073286045681187), (1050, 0.008188052484759224), (1051, 0.0), (1052, 0.01949757886898508), (1053, 0.01130468493347921), (1054, 0.01103699944625331), (1055, 0.0), (1056, 0.0), (1057, 0.02343832337120043), (1058, 0.014326445616965337), (1059, 0.026187328256908955), (1060, 0.025524774616417), (1061, 0.010522732972754849), (1062, 0.0), (1063, 0.0323986861553641), (1064, 0.01723362178999547), (1065, 0.0065346759690377235), (1066, 0.0), (1067, 0.0), (1068, 0.031080086209754408), (1069, 0.007349470531851638), (1070, 0.08104448918225104), (1071, 0.0076296938801074105), (1072, 0.002511969113336023), (1073, 0.0), (1074, 0.018313355636506795), (1075, 0.009591487522932454), (1076, 0.006819943767270469), (1077, 0.00930179774986171), (1078, 0.008004074147420881), (1079, 0.0023322559654003526), (1080, 0.002283153078480931), (1081, 0.0), (1082, 0.004530923132656162), (1083, 0.007438831750066306), (1084, 0.0024851270070419744), (1085, 0.036238762035520095), (1086, 0.0), (1087, 0.009256627090253322), (1088, 0.002168028396331156), (1089, 0.0), (1090, 0.011525766979697764), (1091, 0.0), (1092, 0.009742359298906326), (1093, 0.0), (1094, 0.006428490781993139), (1095, 0.027246132772978986), (1096, 0.008857925187504443), (1097, 0.0), (1098, 0.01988028147728714), (1099, 0.011857342491158735), (1100, 0.002494207439481666), (1101, 0.0), (1102, 0.05016977076463526), (1103, 0.0), (1104, 0.012302637341744903), (1105, 0.0), (1106, 0.0), (1107, 0.013234704742594436), (1108, 0.0), (1109, 0.002812253640075932), (1110, 0.0024929035561424492), (1111, 0.0067125880140789735), (1112, 0.017814761595896286), (1113, 0.0), (1114, 0.014436591435942683), (1115, 0.015076849560100525), (1116, 0.014454249635706785), (1117, 0.0024363948721887476), (1118, 0.05998954734066491), (1119, 0.015187159155518683), (1120, 0.003933222812334196), (1121, 0.0031774370506779245), (1122, 0.0025820607421187945), (1123, 0.006794885124020777), (1124, 0.009439593845048234), (1125, 0.0067987645178981225), (1126, 0.0), (1127, 0.004540712375358485), (1128, 0.01336917289326851), (1129, 0.017757748873229732), (1130, 0.0), (1131, 0.002544645217036425), (1132, 0.020242473075204687), (1133, 0.0), (1134, 0.06151448371353247), (1135, 0.0), (1136, 0.007982223371637606), (1137, 0.027530878040813937), (1138, 0.007232291199342742), (1139, 0.0), (1140, 0.007655221232160154), (1141, 0.022221388090035325), (1142, 0.0), (1143, 0.0), (1144, 0.007259122310498271), (1145, 0.0035070545267648348), (1146, 0.03193270995829649), (1147, 0.0), (1148, 0.05022542698748972), (1149, 0.0), (1150, 0.004975946962821241), (1151, 0.0), (1152, 0.014231082791516454), (1153, 0.0032346284116908913), (1154, 0.004112052748094562), (1155, 0.0), (1156, 0.0), (1157, 0.012054222172340505), (1158, 0.005154276117296022), (1159, 0.0), (1160, 0.00912265594299187), (1161, 0.002289389845898506), (1162, 0.027084968030862168), (1163, 0.0025317112602762436), (1164, 0.0037512621307350573), (1165, 0.0), (1166, 0.0), (1167, 0.005054247756466491), (1168, 0.0030455201632660664), (1169, 0.002968248475121234), (1170, 0.002539030797647179), (1171, 0.0), (1172, 0.006576811496944065), (1173, 0.030413463227986912), (1174, 0.0073090099747231945), (1175, 0.01805082944164325), (1176, 0.0025888535739499907), (1177, 0.0067349171277387735), (1178, 0.0), (1179, 0.007148580085663995), (1180, 0.0), (1181, 0.02490892907408937), (1182, 0.009289577849239705), (1183, 0.013203290150111818), (1184, 0.016227879133609922), (1185, 0.012314336497917706), (1186, 0.023229264871711574), (1187, 0.002979770691711471), (1188, 0.007504203984202115), (1189, 0.0), (1190, 0.0), (1191, 0.007177768471697236), (1192, 0.0143731268998252), (1193, 0.0), (1194, 0.011920690598639651), (1195, 0.03160288863475456), (1196, 0.0), (1197, 0.004241742454974192), (1198, 0.0), (1199, 0.002237279405744827), (1200, 0.0), (1201, 0.0), (1202, 0.019084727907330734), (1203, 0.043288373397248), (1204, 0.002573206584190331), (1205, 0.026572826699719294), (1206, 0.008511491354820998), (1207, 0.004407380155076317), (1208, 0.003233402541827205), (1209, 0.0021134636228278113), (1210, 0.0033546679070800924), (1211, 0.004371438026142519), (1212, 0.0), (1213, 0.006215002337363142), (1214, 0.005932567568348967), (1215, 0.011742448125855624), (1216, 0.016219260534941972), (1217, 0.0022018181096331805), (1218, 0.0), (1219, 0.002275219115804935), (1220, 0.012381759539653547), (1221, 0.0), (1222, 0.0), (1223, 0.00717722505421251), (1224, 0.014848645936442455), (1225, 0.007542388898273974), (1226, 0.018073460855467367), (1227, 0.0), (1228, 0.0), (1229, 0.007464115927586654), (1230, 0.011218996224828769), (1231, 0.006779688354393065), (1232, 0.0143343580423758), (1233, 0.0), (1234, 0.010177649958305484), (1235, 0.0), (1236, 0.03334196963686731), (1237, 0.01291252967933191), (1238, 0.006524049508288304), (1239, 0.013018313167508913), (1240, 0.0), (1241, 0.035270697376675486), (1242, 0.0), (1243, 0.05520158300072489), (1244, 0.0), (1245, 0.01733780597970789), (1246, 0.0), (1247, 0.002449604610534502), (1248, 0.04316322790320628), (1249, 0.011389854850356616), (1250, 0.006695136066226618), (1251, 0.0022442547715836978), (1252, 0.014093237016036804), (1253, 0.0), (1254, 0.016063876077209334), (1255, 0.013034577088155506), (1256, 0.0), (1257, 0.04460086738980612), (1258, 0.0), (1259, 0.010683260447850177), (1260, 0.007892175187202838), (1261, 0.044570869220417475), (1262, 0.011152412806465565), (1263, 0.0), (1264, 0.011577457331668603), (1265, 0.0), (1266, 0.01140830004039545), (1267, 0.006350083320400627), (1268, 0.0), (1269, 0.0), (1270, 0.021212009876187383), (1271, 0.0), (1272, 0.034794423140693004), (1273, 0.00241372964489964), (1274, 0.01759247947637767), (1275, 0.016413131014958164), (1276, 0.008718177494154983), (1277, 0.0018965691925550338), (1278, 0.01469011827176545), (1279, 0.009414733311017304), (1280, 0.004912549776270106), (1281, 0.004210757877745523), (1282, 0.0075637968823544744), (1283, 0.023375973429109315), (1284, 0.002468849236494781), (1285, 0.0), (1286, 0.0024863444285309457), (1287, 0.0), (1288, 0.0), (1289, 0.0), (1290, 0.014782895037111703), (1291, 0.0), (1292, 0.04367380160992527), (1293, 0.012627559394743807), (1294, 0.00260356810870273), (1295, 0.0), (1296, 0.0), (1297, 0.0), (1298, 0.0025221305830124743), (1299, 0.0), (1300, 0.009883442651908877), (1301, 0.002215732627951938), (1302, 0.044531189691413835), (1303, 0.011468723368048096), (1304, 0.0025370239986737347), (1305, 0.0020966909382619018), (1306, 0.0066374175223380336), (1307, 0.006181668255159588), (1308, 0.008353487600809638), (1309, 0.003948380480033668), (1310, 0.011857401788079414), (1311, 0.03394663995212679), (1312, 0.007683696684100865), (1313, 0.0024991701666688348), (1314, 0.026598285558358734), (1315, 0.0), (1316, 0.005910781285140436), (1317, 0.013109511838372383), (1318, 0.0022618699066821774), (1319, 0.0024882460941023266), (1320, 0.0397552488399696), (1321, 0.0), (1322, 0.0), (1323, 0.0), (1324, 0.002705358234925375), (1325, 0.015417810296419088), (1326, 0.0), (1327, 0.006246469827302094), (1328, 0.0), (1329, 0.0064822128175896394), (1330, 0.006945237124300198), (1331, 0.014069567805799925), (1332, 0.005140102469137354), (1333, 0.0), (1334, 0.009866451708928596), (1335, 0.01436626555567386), (1336, 0.0), (1337, 0.01451632001440457), (1338, 0.009453093408532395), (1339, 0.01021596486720332), (1340, 0.002153835131845671), (1341, 0.07732693809361939), (1342, 0.012818109313890115), (1343, 0.013894810017357654), (1344, 0.005721039864961347), (1345, 0.006554266558119459), (1346, 0.0), (1347, 0.004456071224498093), (1348, 0.010181205524417283), (1349, 0.00285762811025138), (1350, 0.002470461927847056), (1351, 0.024875575685802023), (1352, 0.0021543285954857753), (1353, 0.0), (1354, 0.0), (1355, 0.0025971791308945563), (1356, 0.00605131280670182), (1357, 0.0023372106844995522), (1358, 0.0418305667382064), (1359, 0.009783798724744835), (1360, 0.012946114937554584), (1361, 0.015592555033603862), (1362, 0.022486463991498958), (1363, 0.028717455504198453), (1364, 0.002633462452635989), (1365, 0.017784588946112626), (1366, 0.002287746831385266), (1367, 0.03305734622286169), (1368, 0.0), (1369, 0.04027355663153479), (1370, 0.002186813531333692), (1371, 0.007859168909794434), (1372, 0.002379092284915241), (1373, 0.0), (1374, 0.0065735766582562015), (1375, 0.006795276578803917), (1376, 0.012474930782576379), (1377, 0.016773445546711195), (1378, 0.0025340273053027075), (1379, 0.03405703604165394), (1380, 0.004865433624290717), (1381, 0.0052941344423078724), (1382, 0.009398048957401735), (1383, 0.08425242441722802), (1384, 0.017767725898371563), (1385, 0.020819608375770078), (1386, 0.01883315792718334), (1387, 0.008676472959391519), (1388, 0.007105864043348033), (1389, 0.03445912028134007), (1390, 0.0), (1391, 0.005146892045916608), (1392, 0.0022549171667648254), (1393, 0.041789154386127465), (1394, 0.0022470021552231235), (1395, 0.0037135203999899623), (1396, 0.01169412559915647), (1397, 0.021082777924745753), (1398, 0.028222452550706812), (1399, 0.0), (1400, 0.007536440370065782), (1401, 0.01387271954476124), (1402, 0.002659466738009274), (1403, 0.017089358343226592), (1404, 0.0023973664832842947), (1405, 0.028769066044756323), (1406, 0.01142356735170328), (1407, 0.011883388438677927), (1408, 0.0024700615971213528), (1409, 0.0027132641602936663), (1410, 0.0025632853630778354), (1411, 0.0025061728502699713), (1412, 0.023629897886256662), (1413, 0.01392252167553847), (1414, 0.006378299226169405), (1415, 0.002077914644244706), (1416, 0.0024236082196454393), (1417, 0.016231265772845838), (1418, 0.010098426231237303), (1419, 0.011702375166221541), (1420, 0.011136701240334801), (1421, 0.006892431195663454), (1422, 0.0024693633273359873), (1423, 0.002250838550875257), (1424, 0.0), (1425, 0.006682409645770868), (1426, 0.004887726304196335), (1427, 0.0020790061804810836), (1428, 0.0043732088719860346), (1429, 0.008595043377298776), (1430, 0.02653057804103264), (1431, 0.004724038283531271), (1432, 0.012175283212771795), (1433, 0.006651536462062502), (1434, 0.0023155273672975777), (1435, 0.004716569576995678), (1436, 0.012367187829493916), (1437, 0.0), (1438, 0.009518400966834185), (1439, 0.0026554823490857376), (1440, 0.009759613744201243), (1441, 0.0), (1442, 0.0095890271815945), (1443, 0.01831419707001223), (1444, 0.0), (1445, 0.01603828875201241), (1446, 0.008725319988941804), (1447, 0.0), (1448, 0.006606255011892964), (1449, 0.004856782191775572), (1450, 0.0021855787670099175), (1451, 0.004333419161392226), (1452, 0.004876297175437618), (1453, 0.005285281631882958), (1454, 0.00785287184664528), (1455, 0.01167424438890572), (1456, 0.0023540541645859295), (1457, 0.0), (1458, 0.003904651594659914), (1459, 0.0), (1460, 0.0), (1461, 0.013796549363393393), (1462, 0.006557735573350133), (1463, 0.0024452807156080236), (1464, 0.03242600299745582), (1465, 0.013588900862715182), (1466, 0.0), (1467, 0.0), (1468, 0.0), (1469, 0.004775977068505571), (1470, 0.0), (1471, 0.020290800155578558), (1472, 0.007232693801577943), (1473, 0.0), (1474, 0.0028283790706451106), (1475, 0.009491808199921726), (1476, 0.002569492630955095), (1477, 0.008398088250305705), (1478, 0.013621453691624496), (1479, 0.0027816518653624054), (1480, 0.004288052651907407), (1481, 0.01376749105730235), (1482, 0.028603312957890946), (1483, 0.014114297878227612), (1484, 0.007562813857263789), (1485, 0.0), (1486, 0.007234166049300601), (1487, 0.0), (1488, 0.007167547433373899), (1489, 0.008033719451971282), (1490, 0.0), (1491, 0.0), (1492, 0.02171558070297426), (1493, 0.017113614659723917), (1494, 0.009379897367766055), (1495, 0.0), (1496, 0.0), (1497, 0.00289446576555683), (1498, 0.007948536519158821), (1499, 0.030795662279307377), (1500, 0.02729943310930179), (1501, 0.006560512948820128), (1502, 0.004871803904837503), (1503, 0.00229947342488938), (1504, 0.007007295859807677), (1505, 0.021982373147284715), (1506, 0.042282530621225375), (1507, 0.008102011472032189), (1508, 0.0), (1509, 0.014205028339216105), (1510, 0.020480695787819872), (1511, 0.0), (1512, 0.015450085039927697), (1513, 0.010012053684440077), (1514, 0.008426393019628341), (1515, 0.022061747166271108), (1516, 0.0026119169121049377), (1517, 0.0), (1518, 0.0027314707555649094), (1519, 0.012685818153036854), (1520, 0.0), (1521, 0.0), (1522, 0.0), (1523, 0.015826030293870766), (1524, 0.0), (1525, 0.0), (1526, 0.006277220093134095), (1527, 0.03945167296049171), (1528, 0.002303568038250878), (1529, 0.0), (1530, 0.02423044829538496), (1531, 0.00487448226189164), (1532, 0.0), (1533, 0.0025726575647058076), (1534, 0.0), (1535, 0.0), (1536, 0.007357200882370105), (1537, 0.0076545522894884395), (1538, 0.00826452714849783), (1539, 0.008118828372420506), (1540, 0.008264873545767479), (1541, 0.0), (1542, 0.012101632206248939), (1543, 0.0023366207244844292), (1544, 0.02457419064673378), (1545, 0.0), (1546, 0.0039687964989061015), (1547, 0.0029538683671561368), (1548, 0.0), (1549, 0.0), (1550, 0.002500843149361938), (1551, 0.010990327322037603), (1552, 0.0062804575791378355), (1553, 0.008035712147274676), (1554, 0.005079354545010316), (1555, 0.006655728045330869), (1556, 0.0), (1557, 0.0), (1558, 0.0023575804558839345), (1559, 0.003992703732862145), (1560, 0.028142719658602232), (1561, 0.0), (1562, 0.0042731699418304), (1563, 0.0), (1564, 0.0), (1565, 0.0021678323941890097), (1566, 0.004617094549750663), (1567, 0.012359315313796792), (1568, 0.03407235441443471), (1569, 0.0), (1570, 0.0026672319410395466), (1571, 0.007527686704103847), (1572, 0.02474448545068361), (1573, 0.004544910721244759), (1574, 0.0025593435180176335), (1575, 0.00493962475567439), (1576, 0.0036952051361189295), (1577, 0.0), (1578, 0.0), (1579, 0.017412512530218235), (1580, 0.0027985796143798237), (1581, 0.0), (1582, 0.009227189264785263), (1583, 0.007196604196620224), (1584, 0.0), (1585, 0.02294775132215635), (1586, 0.0), (1587, 0.004696037086649698), (1588, 0.004820371979478831), (1589, 0.0), (1590, 0.004022298707395246), (1591, 0.013536957187268665), (1592, 0.0), (1593, 0.003073536197767713), (1594, 0.002839568084275876), (1595, 0.012872864495596305), (1596, 0.0), (1597, 0.0024430773578123536), (1598, 0.002503578013704265), (1599, 0.0), (1600, 0.0), (1601, 0.0), (1602, 0.0), (1603, 0.0), (1604, 0.0), (1605, 0.0022912512467324424), (1606, 0.0), (1607, 0.0), (1608, 0.00631080660484277), (1609, 0.01638052278217861), (1610, 0.0), (1611, 0.0), (1612, 0.009066688687457697), (1613, 0.0), (1614, 0.004935318091384703), (1615, 0.0), (1616, 0.0022287724411460983), (1617, 0.0024759756901920225), (1618, 0.0), (1619, 0.009703084106321473), (1620, 0.008987057234226398), (1621, 0.014022952914941237), (1622, 0.004534966118457996), (1623, 0.0042720073056617385), (1624, 0.0020638114682631757), (1625, 0.0022805657073798956), (1626, 0.0), (1627, 0.006111510124918706), (1628, 0.0023205936685129582), (1629, 0.021463985617207366), (1630, 0.011090579239151285), (1631, 0.004376975220158413), (1632, 0.004423258499538447), (1633, 0.004408178160738385), (1634, 0.027265975858920755), (1635, 0.0045244140400680045), (1636, 0.0), (1637, 0.002720463657139302), (1638, 0.0), (1639, 0.0), (1640, 0.0), (1641, 0.0023518531695646367), (1642, 0.002347271044462082), (1643, 0.00750602651388331), (1644, 0.006561402643121727), (1645, 0.0024501016352676042), (1646, 0.0), (1647, 0.09397055536069451), (1648, 0.029561843201275848), (1649, 0.0), (1650, 0.008442906417332422), (1651, 0.0), (1652, 0.03875069306724735), (1653, 0.0069720422336954115), (1654, 0.012540361812405912), (1655, 0.011075509113125723), (1656, 0.0029077079992601354), (1657, 0.019728179313836136), (1658, 0.0100804736714881), (1659, 0.004917338400093204), (1660, 0.0026498822019617014), (1661, 0.004967986400080027), (1662, 0.010422019588148998), (1663, 0.0023892673771611765), (1664, 0.006221292918029591), (1665, 0.01331864452408986), (1666, 0.0025010320929579662), (1667, 0.01310952332403104), (1668, 0.0), (1669, 0.0), (1670, 0.0026693561451880065), (1671, 0.020621715808903353), (1672, 0.002321722396026475), (1673, 0.0), (1674, 0.007717885024911842), (1675, 0.040396587516422805), (1676, 0.03676900030404152), (1677, 0.001995311917545588), (1678, 0.020674657614782856), (1679, 0.0), (1680, 0.012918757443092243), (1681, 0.012832438035811508), (1682, 0.014708572688973999), (1683, 0.0027139443671448764), (1684, 0.005754002436817411), (1685, 0.009633240613946496), (1686, 0.0), (1687, 0.015081911122046706), (1688, 0.00928447679177188), (1689, 0.0), (1690, 0.008203297599856187), (1691, 0.002164018010334086), (1692, 0.006499365798951296), (1693, 0.00238125826288348), (1694, 0.010377739186490313), (1695, 0.005316808464005938), (1696, 0.010965269002219375), (1697, 0.0), (1698, 0.0), (1699, 0.003991474843652324), (1700, 0.0), (1701, 0.008829989975010642), (1702, 0.03401178055455821), (1703, 0.002624080641588584), (1704, 0.0), (1705, 0.007576217404227394), (1706, 0.002559280265609513), (1707, 0.021603149809261358), (1708, 0.00977923271618291), (1709, 0.0), (1710, 0.00862480157860797), (1711, 0.003180428719665651), (1712, 0.009732335194850533), (1713, 0.041056464531435785), (1714, 0.012011453185764855), (1715, 0.005883156475360245), (1716, 0.015952807160996087), (1717, 0.002611987036217893), (1718, 0.006885352976791461), (1719, 0.002288890438865886), (1720, 0.026475090126577592), (1721, 0.025534461225381583), (1722, 0.0025610950655021386), (1723, 0.010497387610157081), (1724, 0.004967362630089575), (1725, 0.0), (1726, 0.0), (1727, 0.009993058828174554), (1728, 0.0), (1729, 0.0), (1730, 0.008300929366563799), (1731, 0.0), (1732, 0.004930749603787047), (1733, 0.00278081968063316), (1734, 0.0), (1735, 0.007296268013052199), (1736, 0.01006161503112795), (1737, 0.007007001454081945), (1738, 0.006716538657576399), (1739, 0.012790065058483045), (1740, 0.014510564426729732), (1741, 0.015474293874286435), (1742, 0.002398036686183952), (1743, 0.007750090589066046), (1744, 0.002419466647815223), (1745, 0.0), (1746, 0.006130600381762394), (1747, 0.007085757718312184), (1748, 0.002969346654113988), (1749, 0.024814387662836442), (1750, 0.030273505619146518), (1751, 0.0), (1752, 0.03333938657742233), (1753, 0.003965524253339128), (1754, 0.010587649198346934), (1755, 0.0), (1756, 0.0), (1757, 0.021518240078453512), (1758, 0.0), (1759, 0.016900019192624616), (1760, 0.006610240515573115), (1761, 0.011427305445703435), (1762, 0.008122600557858468), (1763, 0.024934636005999537), (1764, 0.007892329915581534), (1765, 0.002623080121500158), (1766, 0.0), (1767, 0.0), (1768, 0.0026075507565416424), (1769, 0.0), (1770, 0.03278254752073779), (1771, 0.0), (1772, 0.004003333399430373), (1773, 0.010955897824683977), (1774, 0.015876691830685904), (1775, 0.0), (1776, 0.008464441636809431), (1777, 0.0), (1778, 0.0), (1779, 0.014605505493867625), (1780, 0.001654444868067222), (1781, 0.00994528192793031), (1782, 0.0023196197449962324), (1783, 0.0), (1784, 0.004189175005907085), (1785, 0.0), (1786, 0.0), (1787, 0.01244311834937289), (1788, 0.029045998553708444), (1789, 0.010793270926753161), (1790, 0.007830652807786428), (1791, 0.004911393510206823), (1792, 0.002980454256720252), (1793, 0.008533810434469269), (1794, 0.0), (1795, 0.029589075994988966), (1796, 0.012978653060000052), (1797, 0.006202669692847393), (1798, 0.009774556470432893), (1799, 0.012247251568054), (1800, 0.0), (1801, 0.002129912236167644), (1802, 0.013074188414515001), (1803, 0.0), (1804, 0.0), (1805, 0.0027632161822077734), (1806, 0.007724060987961749), (1807, 0.008930900977394138), (1808, 0.002274528278954003), (1809, 0.049588147032597375), (1810, 0.0), (1811, 0.007092076580957013), (1812, 0.011945304239266106), (1813, 0.002462243478839766), (1814, 0.002335195713558715), (1815, 0.013530410151107168), (1816, 0.006377671673092274), (1817, 0.020764535380750283), (1818, 0.006224779631552357), (1819, 0.006660823685789856), (1820, 0.0), (1821, 0.04361028830378264), (1822, 0.002677246887881095), (1823, 0.0), (1824, 0.0), (1825, 0.0), (1826, 0.0022933726714825576), (1827, 0.002293422535226092), (1828, 0.0021883753970884136), (1829, 0.005021692709172187), (1830, 0.002247218249834534), (1831, 0.0025076495173526085), (1832, 0.011937535410330451), (1833, 0.0077965095169583885), (1834, 0.0), (1835, 0.0), (1836, 0.0), (1837, 0.03240258300693197), (1838, 0.019939936935035117), (1839, 0.0), (1840, 0.004197512097260954), (1841, 0.006832081872064486), (1842, 0.0), (1843, 0.01777743540800436), (1844, 0.0), (1845, 0.02726613451399632), (1846, 0.004494151496336112), (1847, 0.026430755901808753), (1848, 0.0027301751429851424), (1849, 0.006466697460137597), (1850, 0.04146507077720888), (1851, 0.0026403793617911795), (1852, 0.011027128083942172), (1853, 0.015056577491359779), (1854, 0.009176487834003655), (1855, 0.0), (1856, 0.0), (1857, 0.004541703501595063), (1858, 0.010754515078436713), (1859, 0.004864612361744439), (1860, 0.00936372403435563), (1861, 0.02132668519986058), (1862, 0.0028404195325150506), (1863, 0.005673121301952915), (1864, 0.013194620422679212), (1865, 0.0232913893449777), (1866, 0.007806781469902531), (1867, 0.006487323100488623), (1868, 0.030647250708224397), (1869, 0.0022962581361569956), (1870, 0.011742165690093414), (1871, 0.04119734499545335), (1872, 0.01809054728158338), (1873, 0.011193286227882262), (1874, 0.010386980241245819), (1875, 0.008361119199879558), (1876, 0.013797207843950315), (1877, 0.002420130506591283), (1878, 0.048053795166414184), (1879, 0.0), (1880, 0.014966021703830552), (1881, 0.004825322882698362), (1882, 0.002484915947496337), (1883, 0.0), (1884, 0.0023704895535816193), (1885, 0.0309975246079396), (1886, 0.06267985852941994), (1887, 0.0028740961062598642), (1888, 0.0), (1889, 0.0), (1890, 0.002814173123132308), (1891, 0.0025141756377858905), (1892, 0.006492138216479109), (1893, 0.002674980291477653), (1894, 0.0), (1895, 0.014460083088388845), (1896, 0.002690520691747851), (1897, 0.01487409258896271), (1898, 0.0), (1899, 0.0), (1900, 0.008883222611181612), (1901, 0.004728085067675583), (1902, 0.007514941436228623), (1903, 0.006144808322546005), (1904, 0.004878866675051578), (1905, 0.002765022738371266), (1906, 0.015402172315287378), (1907, 0.0027299453987985325), (1908, 0.0066037384583795015), (1909, 0.0028786576539522103), (1910, 0.003897392208484155), (1911, 0.0068215375429680905), (1912, 0.0), (1913, 0.0064824046591955295), (1914, 0.0043357717271408636), (1915, 0.0), (1916, 0.0026726151622681773), (1917, 0.0), (1918, 0.007551945563332286), (1919, 0.014720185971196648), (1920, 0.008418614385203606), (1921, 0.00226658677711873), (1922, 0.009702305857966465), (1923, 0.010674188244428695), (1924, 0.008167974470972303), (1925, 0.00402731300929992), (1926, 0.0), (1927, 0.019666945381093325), (1928, 0.0), (1929, 0.0024177987312427804), (1930, 0.0046636733428292625), (1931, 0.007304840964451408), (1932, 0.0), (1933, 0.004496946860875293), (1934, 0.012249159605660146), (1935, 0.022777338759990606), (1936, 0.009305710762007566), (1937, 0.01843060245413057), (1938, 0.0), (1939, 0.006122496770723247), (1940, 0.005391940370749308), (1941, 0.005521670047666052), (1942, 0.02115515210916598), (1943, 0.0022075058990114116), (1944, 0.0), (1945, 0.0137474566656582), (1946, 0.002606154682344158), (1947, 0.002944168345871454), (1948, 0.00900217093487605), (1949, 0.012117653116043525), (1950, 0.007437122534097678), (1951, 0.009660200117561584), (1952, 0.004967831528029215), (1953, 0.004482532871190866), (1954, 0.0022466176603640644), (1955, 0.0), (1956, 0.0), (1957, 0.01103713744728498), (1958, 0.011930646176003007), (1959, 0.0027434360138272663), (1960, 0.00791594458958931), (1961, 0.0), (1962, 0.005139410447659317), (1963, 0.0), (1964, 0.006462905219506746), (1965, 0.0), (1966, 0.0), (1967, 0.013818817488233139), (1968, 0.008396226262273387), (1969, 0.0024475444749093773), (1970, 0.05299390678023471), (1971, 0.008146467998911179), (1972, 0.0), (1973, 0.02915657413264359), (1974, 0.0), (1975, 0.004859271928670793), (1976, 0.029555193895324648), (1977, 0.07510309168081497), (1978, 0.0), (1979, 0.0), (1980, 0.00227477464899649), (1981, 0.005908455371472134), (1982, 0.07246569778553744), (1983, 0.014814705291966625), (1984, 0.0), (1985, 0.021011193896198634), (1986, 0.01349344967712845), (1987, 0.006494419384748071), (1988, 0.012449725425893047), (1989, 0.011425033991382281), (1990, 0.0284201409286951), (1991, 0.035376604288887115), (1992, 0.010919745889197363), (1993, 0.004404753943201429), (1994, 0.08287835345252216), (1995, 0.0027271106496794184), (1996, 0.0222321859914211), (1997, 0.023141379590983783), (1998, 0.004669056138259162), (1999, 0.024674542916240657), (2000, 0.012490298103748571), (2001, 0.0), (2002, 0.0), (2003, 0.0), (2004, 0.0023836845211184176), (2005, 0.011813232567949578), (2006, 0.0), (2007, 0.0), (2008, 0.013341066428520627), (2009, 0.0), (2010, 0.0020028590070789534), (2011, 0.025123628978433857), (2012, 0.04293853193777039), (2013, 0.02631318545102932), (2014, 0.030095920732595108), (2015, 0.004817274786074442), (2016, 0.009977672051937518), (2017, 0.0), (2018, 0.03563383095352764), (2019, 0.0), (2020, 0.024235620690403414), (2021, 0.0), (2022, 0.005209538508579561), (2023, 0.030168509278277092), (2024, 0.01362143661567416), (2025, 0.0), (2026, 0.05264268750759823), (2027, 0.0151191157039422), (2028, 0.0), (2029, 0.009383399674635615), (2030, 0.0), (2031, 0.006451642626205173), (2032, 0.0), (2033, 0.0), (2034, 0.002089491496826586), (2035, 0.017841694875906363), (2036, 0.0), (2037, 0.0298193260783485), (2038, 0.0), (2039, 0.0021333513682361693), (2040, 0.022971868335819254), (2041, 0.0), (2042, 0.0), (2043, 0.0), (2044, 0.004900368156440432), (2045, 0.013941721469670178), (2046, 0.0), (2047, 0.0022411341263223567), (2048, 0.025093016553148453), (2049, 0.010037773592981785), (2050, 0.0), (2051, 0.010344755637093042), (2052, 0.01225214405332025), (2053, 0.01468579094084932), (2054, 0.0), (2055, 0.020617915628473392), (2056, 0.006329973382063176), (2057, 0.011335341988602587), (2058, 0.005927826803031612), (2059, 0.0), (2060, 0.0025104283919120114), (2061, 0.007241444441148378), (2062, 0.010827602309256912), (2063, 0.0), (2064, 0.0048383411344764616), (2065, 0.008634933847474484), (2066, 0.013148930864670519), (2067, 0.0025514295143559346), (2068, 0.0024099656054347002), (2069, 0.007024574301463462), (2070, 0.017785602537673223), (2071, 0.0), (2072, 0.0026280155284696), (2073, 0.002584790940607842), (2074, 0.00987182120936709), (2075, 0.009368083693250751), (2076, 0.008106110318529727), (2077, 0.008628455950862961), (2078, 0.0036690612024628845), (2079, 0.0), (2080, 0.009286183430238319), (2081, 0.0), (2082, 0.03137256966163152), (2083, 0.0026541513520933206), (2084, 0.00497883099639507), (2085, 0.0), (2086, 0.0), (2087, 0.00890534030263058), (2088, 0.007490653097136644), (2089, 0.00840106321112749), (2090, 0.0), (2091, 0.00724908335407164), (2092, 0.0), (2093, 0.017353497854371687), (2094, 0.02510748187337649), (2095, 0.00634399459508417), (2096, 0.022163124512581702), (2097, 0.01045894025071592), (2098, 0.005618888882314847), (2099, 0.002370514864288073), (2100, 0.031466640098441356), (2101, 0.007188361400101866), (2102, 0.028465544090018308), (2103, 0.008865792807943298), (2104, 0.0076355178680262425), (2105, 0.0027006582225229704), (2106, 0.0), (2107, 0.0), (2108, 0.0028149681631918447), (2109, 0.03435264766714195), (2110, 0.01675128583620694), (2111, 0.002484294204794003), (2112, 0.06218435141221765), (2113, 0.005140329245801168), (2114, 0.029513454653019616), (2115, 0.0), (2116, 0.009826879593775987), (2117, 0.002432738926313127), (2118, 0.0), (2119, 0.016936626721809577), (2120, 0.0), (2121, 0.013060128472127269), (2122, 0.03310797958980469), (2123, 0.03394554340436231), (2124, 0.0), (2125, 0.0), (2126, 0.009911946717288973), (2127, 0.0021291085789020394), (2128, 0.0), (2129, 0.002350041367477206), (2130, 0.004663428752584404), (2131, 0.0024363566535109513), (2132, 0.002118807318914566), (2133, 0.04895833694100604), (2134, 0.0028368228829513896), (2135, 0.0), (2136, 0.004999931651805338), (2137, 0.0035945925620135804), (2138, 0.0), (2139, 0.004329829930682734), (2140, 0.0), (2141, 0.00242412156867798), (2142, 0.002957911816921575), (2143, 0.00870524190616186), (2144, 0.009184136725802351), (2145, 0.011667846006835805), (2146, 0.0021674057808973805), (2147, 0.032118367696370734), (2148, 0.0026287367207624723), (2149, 0.016711990529519685), (2150, 0.0), (2151, 0.04489615902161054), (2152, 0.0), (2153, 0.0), (2154, 0.026634248456284985), (2155, 0.04005254584556308), (2156, 0.005849206467237161), (2157, 0.02224516374878037), (2158, 0.008249182115915604), (2159, 0.002796642519650155), (2160, 0.006181185621205105), (2161, 0.01649460634120045), (2162, 0.010321303045312511), (2163, 0.0022629965639827504), (2164, 0.0), (2165, 0.0), (2166, 0.002388531571930009), (2167, 0.01780073194851991), (2168, 0.0), (2169, 0.0025525752827928266), (2170, 0.0), (2171, 0.0), (2172, 0.0), (2173, 0.02400710912107853), (2174, 0.02061080199928024), (2175, 0.006065790209232859), (2176, 0.002799738652446759), (2177, 0.013196531145282497), (2178, 0.011369102235506752), (2179, 0.0), (2180, 0.0), (2181, 0.005236538353974075), (2182, 0.0), (2183, 0.0), (2184, 0.0066460697561804795), (2185, 0.00588469360959802), (2186, 0.0), (2187, 0.03763919382653321), (2188, 0.00872547504917266), (2189, 0.0035601273816176465), (2190, 0.0027337675859246567), (2191, 0.050557727650637894), (2192, 0.0025540715080322415), (2193, 0.009187834696774063), (2194, 0.0), (2195, 0.0025294940131200027), (2196, 0.015042495092810679), (2197, 0.009457720469104737), (2198, 0.028466562898500053), (2199, 0.003301396132983232), (2200, 0.0), (2201, 0.002359272840430378), (2202, 0.006188384803965121), (2203, 0.006010749392625514), (2204, 0.0), (2205, 0.006148708939289658), (2206, 0.011172300569001004), (2207, 0.016959411662291247), (2208, 0.0048896326651322545), (2209, 0.010136547687141511), (2210, 0.021656005592106047), (2211, 0.007629219619822573), (2212, 0.036114079291876294), (2213, 0.0022616680757847943), (2214, 0.04836649295986437), (2215, 0.0), (2216, 0.01394089992970633), (2217, 0.0), (2218, 0.0), (2219, 0.0), (2220, 0.0), (2221, 0.028430482696010374), (2222, 0.0), (2223, 0.002883657739557414), (2224, 0.013497855033642384), (2225, 0.0), (2226, 0.0024799385815856712), (2227, 0.0), (2228, 0.009156965667265397), (2229, 0.015545140188962478), (2230, 0.0026046209600846023), (2231, 0.00509809890783702), (2232, 0.0045071342704136605), (2233, 0.0), (2234, 0.0), (2235, 0.012010628945253024), (2236, 0.008262153855153739), (2237, 0.018480469432030938), (2238, 0.0), (2239, 0.006407566328685134), (2240, 0.0022256256462686403), (2241, 0.0), (2242, 0.0024106327127107344), (2243, 0.0), (2244, 0.007224478463281346), (2245, 0.0044559238644446015), (2246, 0.004604721551112668), (2247, 0.0), (2248, 0.04144905622988321), (2249, 0.0), (2250, 0.009590492035507887), (2251, 0.003528765524922965), (2252, 0.012593659017289198), (2253, 0.0), (2254, 0.015264388099765314), (2255, 0.009224149251331642), (2256, 0.0), (2257, 0.003265288941763766), (2258, 0.016645098924895147), (2259, 0.0), (2260, 0.002713062173204411), (2261, 0.0), (2262, 0.0), (2263, 0.0), (2264, 0.00853872494735178), (2265, 0.008265713268684284), (2266, 0.0031228492472702065), (2267, 0.0), (2268, 0.002449391524423003), (2269, 0.0029435278244624215), (2270, 0.00219130592332667), (2271, 0.0), (2272, 0.0), (2273, 0.005445167150185859), (2274, 0.0), (2275, 0.015828663325572444), (2276, 0.02602103823289531), (2277, 0.009229634965057291), (2278, 0.004680281026963687), (2279, 0.009364676134641814), (2280, 0.011578581065887973), (2281, 0.0), (2282, 0.0), (2283, 0.004916374937626596), (2284, 0.014301377390974099), (2285, 0.008192880614420481), (2286, 0.0032411344327654677), (2287, 0.002115909997010881), (2288, 0.002682616857696323), (2289, 0.0025186187714120985), (2290, 0.015664174994228695), (2291, 0.005627749684426434), (2292, 0.0025830825071317524), (2293, 0.0027644911596349914), (2294, 0.04801663260090347), (2295, 0.03982190635490875), (2296, 0.0), (2297, 0.0), (2298, 0.01514742367875594), (2299, 0.004055627755214389), (2300, 0.0), (2301, 0.020346391053315458), (2302, 0.0028806560860410685), (2303, 0.008587247057459328), (2304, 0.007905045081506133), (2305, 0.0), (2306, 0.011519597561857308), (2307, 0.0), (2308, 0.03786870914432212), (2309, 0.00869760131422764), (2310, 0.0033909407420161346), (2311, 0.0), (2312, 0.0), (2313, 0.0025749114546800315), (2314, 0.005075043982713094), (2315, 0.0), (2316, 0.03605001327712352), (2317, 0.002346650633681952), (2318, 0.05698746413620388), (2319, 0.0026346960439084625), (2320, 0.0029483683178666044), (2321, 0.04096332211047457), (2322, 0.0), (2323, 0.002288710033556969), (2324, 0.006544521660283181), (2325, 0.0), (2326, 0.0036225713051403125), (2327, 0.0), (2328, 0.005662324030417309), (2329, 0.0), (2330, 0.004877726866423949), (2331, 0.0), (2332, 0.0), (2333, 0.0), (2334, 0.014641018727413668), (2335, 0.006626868445508635), (2336, 0.011622841866254629), (2337, 0.0), (2338, 0.0022913946207671343), (2339, 0.0074607042887312154), (2340, 0.002542464113880335), (2341, 0.0), (2342, 0.0), (2343, 0.02760157045044117), (2344, 0.007164432520815709), (2345, 0.0), (2346, 0.01092789141982469), (2347, 0.016442297909857247), (2348, 0.00673431186581514), (2349, 0.003511569740426779), (2350, 0.00325898047079926), (2351, 0.0), (2352, 0.0), (2353, 0.015804215693918204), (2354, 0.002538709830463113), (2355, 0.005960565575827434), (2356, 0.002835167909469329), (2357, 0.0), (2358, 0.05826769637272555), (2359, 0.0021168368849086407), (2360, 0.0), (2361, 0.0026901282387533547), (2362, 0.019305653311181028), (2363, 0.008743311125802651), (2364, 0.0), (2365, 0.03251802786423902), (2366, 0.013612976268805008), (2367, 0.0024277017381169885), (2368, 0.018295323351875652), (2369, 0.0), (2370, 0.002642265734795532), (2371, 0.03544860769227722), (2372, 0.0), (2373, 0.0), (2374, 0.047351480752962534), (2375, 0.036029161296792664), (2376, 0.015381706835274796), (2377, 0.0), (2378, 0.002984702466710939), (2379, 0.0036601865946633357), (2380, 0.0), (2381, 0.0), (2382, 0.002172550292225871), (2383, 0.012996311044988591), (2384, 0.0), (2385, 0.0026712362062835497), (2386, 0.00259294748990694), (2387, 0.002530666096103633), (2388, 0.006227393088748629), (2389, 0.0), (2390, 0.00278029308266928), (2391, 0.0027087775163753196), (2392, 0.0033114422157635385), (2393, 0.0027065538121768627), (2394, 0.02568905521652685), (2395, 0.0), (2396, 0.0025592317330554275), (2397, 0.002579374719519521), (2398, 0.0), (2399, 0.0023410933373043154), (2400, 0.0028685555016257766), (2401, 0.002464829336269373), (2402, 0.002296822088102547), (2403, 0.010494032014463658), (2404, 0.0034495650395905005), (2405, 0.0026377860013835812), (2406, 0.016708556127859726), (2407, 0.003505785923314623), (2408, 0.024729842506337994), (2409, 0.0), (2410, 0.0027822668653526748), (2411, 0.0028718128480025207), (2412, 0.012351300951143736), (2413, 0.029928886003016544), (2414, 0.0), (2415, 0.0030774782113262584), (2416, 0.0024995988683299913), (2417, 0.048975289561833585), (2418, 0.009651250070554153), (2419, 0.002664517725272706), (2420, 0.0), (2421, 0.011393352490635826), (2422, 0.0024618756983894995), (2423, 0.003196216137743943), (2424, 0.006412851568886809), (2425, 0.003286983090237742), (2426, 0.005920751565415964), (2427, 0.008304726949703233), (2428, 0.007890164359013144), (2429, 0.010834879177906962), (2430, 0.002573152120809181), (2431, 0.0), (2432, 0.004446831956179276), (2433, 0.0), (2434, 0.0030319578792125535), (2435, 0.0), (2436, 0.0101763666679201), (2437, 0.0028786888060857926), (2438, 0.003141434949500873), (2439, 0.005393098007991499), (2440, 0.020740361118753315), (2441, 0.002053736643431966), (2442, 0.004290553298955562), (2443, 0.029803434615890047), (2444, 0.007216822945365926), (2445, 0.0), (2446, 0.0023555939250982988), (2447, 0.012200094819470354), (2448, 0.003312180628444434), (2449, 0.021985066932388473), (2450, 0.0), (2451, 0.0), (2452, 0.0), (2453, 0.002330973019391161), (2454, 0.0030625130786813577), (2455, 0.0), (2456, 0.0), (2457, 0.002281400117753307), (2458, 0.0), (2459, 0.0087021962221496), (2460, 0.013377406312830293), (2461, 0.0024590433491334033), (2462, 0.0), (2463, 0.00894983822573773), (2464, 0.010540963361888974), (2465, 0.0), (2466, 0.0026046209947012903), (2467, 0.02552401265792079), (2468, 0.013656866052808383), (2469, 0.019146859249126912), (2470, 0.0), (2471, 0.0), (2472, 0.0), (2473, 0.008671326295738156), (2474, 0.012025234810505206), (2475, 0.0027274386737216644), (2476, 0.03244347050543419), (2477, 0.007724564644052247), (2478, 0.002911461177243871), (2479, 0.0), (2480, 0.011086109421716206), (2481, 0.02847926123774087), (2482, 0.0023377306593093767), (2483, 0.0), (2484, 0.02391517705724991), (2485, 0.0), (2486, 0.013345114807622599), (2487, 0.0281679357752627), (2488, 0.0030994924411226936), (2489, 0.009794792049552446), (2490, 0.003655433841287204), (2491, 0.0), (2492, 0.0025520544443002457), (2493, 0.0), (2494, 0.009816473373279778), (2495, 0.0025359570773834284), (2496, 0.006686100058633569), (2497, 0.0), (2498, 0.0), (2499, 0.0), (2500, 0.0), (2501, 0.020059505094761957), (2502, 0.00223764903510972), (2503, 0.006513803988319437), (2504, 0.0), (2505, 0.010111741990795405), (2506, 0.004628370144810393), (2507, 0.002755050857258632), (2508, 0.0), (2509, 0.0020841748846264375), (2510, 0.007529972715630197), (2511, 0.0), (2512, 0.009542271470272569), (2513, 0.018276897871510427), (2514, 0.0), (2515, 0.0), (2516, 0.0), (2517, 0.031513234738017475), (2518, 0.0), (2519, 0.007297888997678442), (2520, 0.0021985696707984234), (2521, 0.0), (2522, 0.015160218557647749), (2523, 0.0), (2524, 0.020004759477924062), (2525, 0.0023881792409710723), (2526, 0.0020750832006275386), (2527, 0.0021813091911791218), (2528, 0.0023552329351234197), (2529, 0.0036815468729244245), (2530, 0.04481510146028207), (2531, 0.0026431568888262663), (2532, 0.0), (2533, 0.0025508245122476576), (2534, 0.0011313649045941105), (2535, 0.0028109713012137647), (2536, 0.0), (2537, 0.0034791458040229705), (2538, 0.06802035746289192), (2539, 0.0), (2540, 0.037262447116274064), (2541, 0.003914935281133384), (2542, 0.0), (2543, 0.0), (2544, 0.002950977553805173), (2545, 0.00948600870856867), (2546, 0.010005453203518996), (2547, 0.0), (2548, 0.0), (2549, 0.0), (2550, 0.04836540834452215), (2551, 0.0), (2552, 0.0023711683412701526), (2553, 0.01743749009788074), (2554, 0.002558519538702846), (2555, 0.011014281773315506), (2556, 0.0023516975035823683), (2557, 0.003145443106586993), (2558, 0.08267633224298852), (2559, 0.0033339816446641937), (2560, 0.024171741903165515), (2561, 0.0026459399529272696), (2562, 0.0), (2563, 0.007530270288055348), (2564, 0.0), (2565, 0.00965865847843089), (2566, 0.0), (2567, 0.005474566349004076), (2568, 0.011135731584107677), (2569, 0.0025060501697395116), (2570, 0.002985006527074178), (2571, 0.0024503212988856386), (2572, 0.008624926760274992), (2573, 0.0037816412403020687), (2574, 0.0), (2575, 0.0), (2576, 0.0052191298618978746), (2577, 0.0), (2578, 0.0), (2579, 0.048167961252127585), (2580, 0.0063848130308622525), (2581, 0.008841135380210335), (2582, 0.020104138588029275), (2583, 0.0), (2584, 0.0), (2585, 0.002823318914999516), (2586, 0.0), (2587, 0.00808003809866371), (2588, 0.0), (2589, 0.0), (2590, 0.0), (2591, 0.002275344532719518), (2592, 0.0028077159504372807), (2593, 0.002339930796183013), (2594, 0.0), (2595, 0.0027508174308408452), (2596, 0.0), (2597, 0.0), (2598, 0.021287142760911603), (2599, 0.004986212320267052), (2600, 0.008926105435859566), (2601, 0.009495593230104763), (2602, 0.011802879057726746), (2603, 0.007647101042214018), (2604, 0.0), (2605, 0.0), (2606, 0.007198949096365795), (2607, 0.01863811941695475), (2608, 0.0), (2609, 0.0027051460174360585), (2610, 0.0026802854429516182), (2611, 0.0021758158812791722), (2612, 0.0024494145037263775), (2613, 0.002987833615753465), (2614, 0.029225820521244943), (2615, 0.0), (2616, 0.0), (2617, 0.012541240022816237), (2618, 0.01901317620959763), (2619, 0.0030541950397158135), (2620, 0.0), (2621, 0.031445444080265395), (2622, 0.03748821698202329), (2623, 0.0028711452225422974), (2624, 0.002775130272788046), (2625, 0.011042436956048845), (2626, 0.00506321164286469), (2627, 0.0), (2628, 0.0033200750239033732), (2629, 0.0028789827889471042), (2630, 0.04898534827274639), (2631, 0.0), (2632, 0.013395941670378386), (2633, 0.009558772985519754), (2634, 0.0023697651035010894), (2635, 0.008290017471095085), (2636, 0.0019040719219632182), (2637, 0.0), (2638, 0.023625589296039667), (2639, 0.015060665745970907), (2640, 0.009526668488920899), (2641, 0.0), (2642, 0.0024435014093075946), (2643, 0.003280052907901832), (2644, 0.014605903574472971), (2645, 0.01830642082683205), (2646, 0.021358135818460758), (2647, 0.02278830310814006), (2648, 0.0), (2649, 0.0235700589676888), (2650, 0.018583354119550942), (2651, 0.002399527090955675), (2652, 0.002563989720311715), (2653, 0.04697351928240422), (2654, 0.016882448039672114), (2655, 0.009474781634864609), (2656, 0.0), (2657, 0.0), (2658, 0.0), (2659, 0.0), (2660, 0.004289301064415874), (2661, 0.0027225967815229855), (2662, 0.0), (2663, 0.0), (2664, 0.002703826942826442), (2665, 0.005408896703823956), (2666, 0.0), (2667, 0.0), (2668, 0.021394926823283075), (2669, 0.0), (2670, 0.0), (2671, 0.0), (2672, 0.0), (2673, 0.0033738107663759957), (2674, 0.002334618638576613), (2675, 0.0), (2676, 0.0), (2677, 0.0), (2678, 0.004130445306673907), (2679, 0.002399906962190324), (2680, 0.010718798803295179), (2681, 0.0), (2682, 0.00430424398851454), (2683, 0.0051675037568785385), (2684, 0.0), (2685, 0.0), (2686, 0.0), (2687, 0.026027725036469426), (2688, 0.011271200116927366), (2689, 0.024527497165292594), (2690, 0.0), (2691, 0.006834099053790853), (2692, 1.0000000000000002), (2693, 0.0), (2694, 0.04368554902472678), (2695, 0.014242176019135196), (2696, 0.0029482119642483444), (2697, 0.011645129052455468), (2698, 0.008871041588029817), (2699, 0.02329919140759537), (2700, 0.005182671029789315), (2701, 0.0), (2702, 0.0028986752398810866), (2703, 0.0), (2704, 0.0), (2705, 0.0027461280207631174), (2706, 0.029422744288845587), (2707, 0.0029766094818745683), (2708, 0.006695604248962895), (2709, 0.0), (2710, 0.02988730591823796), (2711, 0.004389725240886559), (2712, 0.016746711251381167), (2713, 0.023432161916103617), (2714, 0.007566646462252822), (2715, 0.0), (2716, 0.03603309472599682), (2717, 0.0), (2718, 0.02319674459478677), (2719, 0.0), (2720, 0.0029724638078420245), (2721, 0.0022037253425713542), (2722, 0.0035603643441040962), (2723, 0.02837260039695167), (2724, 0.00635309231256632), (2725, 0.002712359055125161), (2726, 0.006782846187248172), (2727, 0.014058481372388208), (2728, 0.0023085003156347404), (2729, 0.0), (2730, 0.0), (2731, 0.003404339062511265), (2732, 0.006699254917744875), (2733, 0.005124706672572313), (2734, 0.0), (2735, 0.002341654335424115), (2736, 0.01900887034546454), (2737, 0.0), (2738, 0.002992961118255661), (2739, 0.010547486722511865), (2740, 0.01025165340770671), (2741, 0.0022835488818161043), (2742, 0.0169510462112069), (2743, 0.002174428378375937), (2744, 0.009436372522052039), (2745, 0.04326153862816202), (2746, 0.0025787071567579885), (2747, 0.0021975775185931763), (2748, 0.0027578844179992276), (2749, 0.0), (2750, 0.0), (2751, 0.03186976241331189), (2752, 0.009192679728709074), (2753, 0.0022342808694140515), (2754, 0.0), (2755, 0.0026817901026760537), (2756, 0.0), (2757, 0.0038818149563784156), (2758, 0.002153957079075249), (2759, 0.010896125543937797), (2760, 0.018712458702392774), (2761, 0.025056785877878327), (2762, 0.025980223803704138), (2763, 0.0), (2764, 0.003613273940570898), (2765, 0.0024107410707284744), (2766, 0.0020124065471371724), (2767, 0.019020439331965698), (2768, 0.02022019513311771), (2769, 0.01074689549252221), (2770, 0.0), (2771, 0.012070015475522526), (2772, 0.003004298617678023), (2773, 0.0), (2774, 0.005249022144044434), (2775, 0.003443022569045042), (2776, 0.0027315257028121924), (2777, 0.02151782398151878), (2778, 0.00864507950538454), (2779, 0.0024210805376161204), (2780, 0.012102460227641368), (2781, 0.0), (2782, 0.029448976097656177), (2783, 0.002552340094267794), (2784, 0.01453920272142293), (2785, 0.0), (2786, 0.002715966686361918), (2787, 0.004386794249015826), (2788, 0.011899567306988528), (2789, 0.009294840803167722), (2790, 0.004850603519905103), (2791, 0.027708494673946583), (2792, 0.0026869471767721692), (2793, 0.0), (2794, 0.0), (2795, 0.017963854794401393), (2796, 0.002902421975777824), (2797, 0.003104258374734227), (2798, 0.00924585532579227), (2799, 0.0), (2800, 0.002396136918108817), (2801, 0.003957482166523577), (2802, 0.02690014016428078), (2803, 0.012484307978364386), (2804, 0.0), (2805, 0.013422971549413958), (2806, 0.0), (2807, 0.030117994968785384), (2808, 0.020148475915238922), (2809, 0.005339089482851617), (2810, 0.0), (2811, 0.0), (2812, 0.00858075314838778), (2813, 0.0), (2814, 0.0), (2815, 0.014233614635509399), (2816, 0.006796760437225053), (2817, 0.0), (2818, 0.0), (2819, 0.004887152493105063), (2820, 0.009780711952702378), (2821, 0.002692429842320299), (2822, 0.0215532629683982), (2823, 0.01753869196282759), (2824, 0.0), (2825, 0.00698930913622386), (2826, 0.002549723716021327), (2827, 0.0), (2828, 0.0), (2829, 0.0), (2830, 0.0028226149209496683), (2831, 0.00911547050081377), (2832, 0.003328358371392943), (2833, 0.006306426535276037), (2834, 0.00314646446990567), (2835, 0.0), (2836, 0.0), (2837, 0.0), (2838, 0.0032411818306879335), (2839, 0.0), (2840, 0.007974038146102615), (2841, 0.01969468096073799), (2842, 0.0), (2843, 0.007294454990914622), (2844, 0.007519917586582681), (2845, 0.0023343307734320145), (2846, 0.04034937166874806), (2847, 0.004554869102789387), (2848, 0.0030957310537843), (2849, 0.010160919483403277), (2850, 0.0), (2851, 0.0), (2852, 0.0), (2853, 0.0025234742839204257), (2854, 0.007940287278032943), (2855, 0.0), (2856, 0.0), (2857, 0.0031306293625923613), (2858, 0.003594793230747527), (2859, 0.03892062672772363), (2860, 0.0), (2861, 0.003361654585292839), (2862, 0.00236358722606658), (2863, 0.002614997779838141), (2864, 0.0), (2865, 0.0), (2866, 0.0), (2867, 0.019569346792707398), (2868, 0.03471057850484338), (2869, 0.040554179176207086), (2870, 0.0034381012735800014), (2871, 0.010392979560845669), (2872, 0.002919385177617543), (2873, 0.007460728637960147), (2874, 0.01266304370471334), (2875, 0.0), (2876, 0.02775849524463103), (2877, 0.0), (2878, 0.0026734722698293838), (2879, 0.008707067714400177), (2880, 0.0), (2881, 0.008097352464452926), (2882, 0.0027559720055843886), (2883, 0.003432062958059232), (2884, 0.002927723897692589), (2885, 0.01553066265467311), (2886, 0.009169658422198456), (2887, 0.029503613070800693), (2888, 0.0027472806692475423), (2889, 0.003491315543824116), (2890, 0.0027985606578063223), (2891, 0.0), (2892, 0.0024074500325428775), (2893, 0.043187343639666156), (2894, 0.0026026276553647375), (2895, 0.003035734397694937), (2896, 0.0), (2897, 0.0067578748204000574), (2898, 0.0), (2899, 0.006720886243817159), (2900, 0.002528116234955642), (2901, 0.003256227513237159), (2902, 0.0018652926953995987), (2903, 0.10063787314386034), (2904, 0.002637905178614227), (2905, 0.0), (2906, 0.0), (2907, 0.0023521461999904784), (2908, 0.03473069779062641), (2909, 0.002473493900684701), (2910, 0.013917633478282367), (2911, 0.002639526247691848), (2912, 0.026637958351887214), (2913, 0.01160626617783045), (2914, 0.002868252351944781), (2915, 0.009901438303503266), (2916, 0.0028408048332358568), (2917, 0.01597938404955991), (2918, 0.01126091009960449), (2919, 0.014694787924982376), (2920, 0.02664140279351682), (2921, 0.0), (2922, 0.0), (2923, 0.003417166947221909), (2924, 0.002941313927795408), (2925, 0.01142089851991689), (2926, 0.0026523761741113687), (2927, 0.0), (2928, 0.0), (2929, 0.00997316401811581), (2930, 0.0), (2931, 0.014636190656546155), (2932, 0.018807248735502158), (2933, 0.007732280496939367), (2934, 0.009681263395234521), (2935, 0.005833966818310372), (2936, 0.010306943195722024), (2937, 0.0036418513127225525), (2938, 0.0), (2939, 0.014557655967115493), (2940, 0.002710772343352202), (2941, 0.0), (2942, 0.00787876782175488), (2943, 0.0025270661897384182), (2944, 0.050454430002777675), (2945, 0.0024825994654153038), (2946, 0.0024959286076673085), (2947, 0.004728489945670273), (2948, 0.009213541283917926), (2949, 0.007639155147339895), (2950, 0.023732959516752646), (2951, 0.0), (2952, 0.0), (2953, 0.002684490889512162), (2954, 0.002315748814608356), (2955, 0.0), (2956, 0.0), (2957, 0.0031027576887766853), (2958, 0.0), (2959, 0.004856626562989746), (2960, 0.004705331125110952), (2961, 0.014001569133349953), (2962, 0.006732649301460031), (2963, 0.012480046815579984), (2964, 0.00972958693050268), (2965, 0.0024091872105101776), (2966, 0.003083110206798772), (2967, 0.0), (2968, 0.0), (2969, 0.012999702326476783), (2970, 0.0027032949511497564), (2971, 0.044168735616715235), (2972, 0.025931096430882088), (2973, 0.0), (2974, 0.002847448826702877), (2975, 0.00799910472417184), (2976, 0.0022719244680200154), (2977, 0.009322674076250256), (2978, 0.012709399900374011), (2979, 0.0), (2980, 0.00892969508928226), (2981, 0.03442583219886153), (2982, 0.0), (2983, 0.0), (2984, 0.004235521067904496), (2985, 0.05717355295839895), (2986, 0.0029999075948067633), (2987, 0.0029279224859267345), (2988, 0.014148959205037389), (2989, 0.003533948201952056), (2990, 0.0), (2991, 0.0046748260207572076), (2992, 0.010426386435022177), (2993, 0.003059036294957494), (2994, 0.0071209261581707105), (2995, 0.01996032958314584), (2996, 0.01565414109129707), (2997, 0.0023971601065590838), (2998, 0.003807469070934451), (2999, 0.0025217999584430033), (3000, 0.018313196560767752), (3001, 0.0), (3002, 0.0), (3003, 0.002817373993822036), (3004, 0.032584681512207773), (3005, 0.004662843276282043), (3006, 0.0), (3007, 0.002709427775494519), (3008, 0.007343589760949153), (3009, 0.0), (3010, 0.0475919192650606), (3011, 0.004454894047740582), (3012, 0.015947957006243817), (3013, 0.0028610165731193576), (3014, 0.0023942259924392586), (3015, 0.0032138288529427426), (3016, 0.0026036229481642107), (3017, 0.025952831108870544), (3018, 0.007388671328103669), (3019, 0.016559249698570755), (3020, 0.0030788992114505528), (3021, 0.0), (3022, 0.005367062238452818), (3023, 0.04447257244459566), (3024, 0.002098006477285881), (3025, 0.0), (3026, 0.002802065432959627), (3027, 0.0022822077528129765), (3028, 0.026584450169584505), (3029, 0.0), (3030, 0.0034357627126280015), (3031, 0.003098080340964135), (3032, 0.008002698145813185), (3033, 0.006565105720620909), (3034, 0.0), (3035, 0.00680633588123159), (3036, 0.01700523802225701), (3037, 0.0026770809629725915), (3038, 0.0), (3039, 0.007433241299459784), (3040, 0.003541823977779952), (3041, 0.0), (3042, 0.0034363661000082163), (3043, 0.016102860661864705), (3044, 0.002764551763558158), (3045, 0.03500487119962276), (3046, 0.008930165950430557), (3047, 0.0), (3048, 0.0), (3049, 0.00572814392853459), (3050, 0.002323618032452493), (3051, 0.003617701658361142), (3052, 0.003464159943233294), (3053, 0.0732438108456325), (3054, 0.0), (3055, 0.0034510966937722886), (3056, 0.002101035489155866), (3057, 0.0023791981149129493), (3058, 0.0), (3059, 0.0), (3060, 0.0), (3061, 0.0), (3062, 0.0028117656637352906), (3063, 0.0), (3064, 0.0027596699778360194), (3065, 0.011652341121195921), (3066, 0.006417860970259336), (3067, 0.008994762392335234), (3068, 0.021254290997707096), (3069, 0.0024767080275248632), (3070, 0.01044100980493831), (3071, 0.0023755248561706534), (3072, 0.0029477207530535492), (3073, 0.0), (3074, 0.0031116199020941445), (3075, 0.002463151112658168), (3076, 0.012578428563124638), (3077, 0.0), (3078, 0.0), (3079, 0.004251719719739137), (3080, 0.0), (3081, 0.002984739096348554), (3082, 0.0), (3083, 0.020305822398005775), (3084, 0.0026899001407307507), (3085, 0.017441414767477733), (3086, 0.01536640033114927), (3087, 0.0), (3088, 0.0), (3089, 0.0), (3090, 0.0), (3091, 0.04501840790205196), (3092, 0.0), (3093, 0.0024959578802307074), (3094, 0.010653611691713995), (3095, 0.02232378376646734), (3096, 0.00791471142124377), (3097, 0.018399578507274313), (3098, 0.01682852088519415), (3099, 0.010396584806118781), (3100, 0.0043093976297925605), (3101, 0.002801975252648181), (3102, 0.03452469488743669), (3103, 0.0), (3104, 0.0), (3105, 0.0), (3106, 0.0), (3107, 0.0), (3108, 0.012312576591772555), (3109, 0.0), (3110, 0.013148818620795283), (3111, 0.018849760702424365), (3112, 0.007688011853815088), (3113, 0.0025867747290768866), (3114, 0.006072588491821387), (3115, 0.0), (3116, 0.0027869581898004835), (3117, 0.005288750302616192), (3118, 0.010846767325738211), (3119, 0.013176467645873434), (3120, 0.008898319654514026), (3121, 0.0), (3122, 0.0068204751632027355), (3123, 0.008720722046885655), (3124, 0.0047897235355676224), (3125, 0.0071848861424403995), (3126, 0.004418094007533676), (3127, 0.036590721490267514), (3128, 0.003197007951514602), (3129, 0.01715175212683575), (3130, 0.0), (3131, 0.004935719359181448), (3132, 0.0), (3133, 0.004336292620515619), (3134, 0.004815055879995134), (3135, 0.004320968927313894), (3136, 0.004302789301984928), (3137, 0.03279268523839364), (3138, 0.0), (3139, 0.0035907551640025526), (3140, 0.003191775106003641), (3141, 0.0), (3142, 0.009781933944899053), (3143, 0.004284662611376249), (3144, 0.01868398340994474), (3145, 0.0), (3146, 0.02959142995417388), (3147, 0.0023610495805435113), (3148, 0.0028715022964075974), (3149, 0.0068243582803357815), (3150, 0.0026535302094216734), (3151, 0.008673167385631366), (3152, 0.007105099502527769), (3153, 0.023168777515517318), (3154, 0.02606963846967903), (3155, 0.009676985323238005), (3156, 0.025482070893600085), (3157, 0.030753179174541134), (3158, 0.005170714049097465), (3159, 0.003138905401171387), (3160, 0.004052363978554839), (3161, 0.004551187168761801), (3162, 0.0), (3163, 0.005021375235815922), (3164, 0.0055627503744931995), (3165, 0.0029129982157773643), (3166, 0.0035179839931373026), (3167, 0.026076234240691325), (3168, 0.0051948318476039), (3169, 0.0), (3170, 0.0024127694654795177), (3171, 0.009142617878024973), (3172, 0.0), (3173, 0.0024976685366919467), (3174, 0.02743679517966769), (3175, 0.0), (3176, 0.0), (3177, 0.0), (3178, 0.004009837888876761), (3179, 0.004737186136549798), (3180, 0.005132573372863185), (3181, 0.0), (3182, 0.0025835580046934636), (3183, 0.002777237875199438), (3184, 0.002724037993344761), (3185, 0.007000170786572425), (3186, 0.002875686598671847), (3187, 0.0026688975569496218), (3188, 0.0), (3189, 0.0), (3190, 0.0), (3191, 0.004749484075312184), (3192, 0.007816038194544937), (3193, 0.0), (3194, 0.002393826048162591), (3195, 0.007035857525779765), (3196, 0.008017179405249625), (3197, 0.0), (3198, 0.002619974529864259), (3199, 0.0019640006274080314), (3200, 0.0021549128346638855), (3201, 0.0), (3202, 0.0), (3203, 0.0498349227897459), (3204, 0.0), (3205, 0.004886156117287779), (3206, 0.003068521345130194), (3207, 0.0), (3208, 0.0), (3209, 0.0404720498947614), (3210, 0.01434822359640147), (3211, 0.0021958742889033934), (3212, 0.0), (3213, 0.016734398067455605), (3214, 0.0024212685427485426), (3215, 0.009351852172126342), (3216, 0.002523810162634958), (3217, 0.0), (3218, 0.00970686767527964), (3219, 0.003314404248274218), (3220, 0.002478699076060922), (3221, 0.0), (3222, 0.02092202862294061), (3223, 0.0), (3224, 0.002640477416532266), (3225, 0.002598945361261664), (3226, 0.016748323767747708), (3227, 0.00720882098845807), (3228, 0.01664828857203829), (3229, 0.0), (3230, 0.0029279919041756575), (3231, 0.0), (3232, 0.010219438024982971), (3233, 0.007355187520740297), (3234, 0.002772188328120311), (3235, 0.002703665113092289), (3236, 0.0), (3237, 0.008993087333431068), (3238, 0.0021825937843072797), (3239, 0.0031975367271760966), (3240, 0.011249340870596558), (3241, 0.0026458927031980622), (3242, 0.0026627240239371097), (3243, 0.0023753766953138553), (3244, 0.006017414560259967), (3245, 0.007148416664097887), (3246, 0.008728646467293667), (3247, 0.004172448145238135), (3248, 0.06683400770968473), (3249, 0.04101786522213684), (3250, 0.0), (3251, 0.0), (3252, 0.002113286442481704), (3253, 0.014939900433374384), (3254, 0.019934000066389027), (3255, 0.033861184392018406), (3256, 0.0076572783933819), (3257, 0.003055972375457137), (3258, 0.0027578268313340052), (3259, 0.007461484276829566), (3260, 0.025956117613509078), (3261, 0.0), (3262, 0.0032633245940029516), (3263, 0.005025888185502877), (3264, 0.009614029034340891), (3265, 0.006769470229076111), (3266, 0.0), (3267, 0.00872099401762529), (3268, 0.0024206147492601745), (3269, 0.0027434131677741983), (3270, 0.0), (3271, 0.0027403415978842337), (3272, 0.0), (3273, 0.00282353327570058), (3274, 0.0028575753057830207), (3275, 0.016625701732328566), (3276, 0.11904275527845871), (3277, 0.0), (3278, 0.002306109060903631), (3279, 0.01710645888961131), (3280, 0.03633050021075282), (3281, 0.0), (3282, 0.0032890614008540533), (3283, 0.0025832882921760798), (3284, 0.018580379689813888), (3285, 0.024986270155456007), (3286, 0.0), (3287, 0.0), (3288, 0.006427108303657308), (3289, 0.002599146485402696), (3290, 0.0026100030058059252), (3291, 0.0034081886534521894), (3292, 0.0033107771042186927), (3293, 0.009096992545310073), (3294, 0.04624323347380142), (3295, 0.01396915092951471), (3296, 0.0028845687282931273), (3297, 0.010212639038269283), (3298, 0.002449889141972864), (3299, 0.015574789122903308), (3300, 0.0023833694605941173), (3301, 0.0019860420011163526), (3302, 0.003090102959529381), (3303, 0.0072756740838892334), (3304, 0.0022964795595691884), (3305, 0.0), (3306, 0.0152976874344642), (3307, 0.0029460254497445243), (3308, 0.0030025452049455338), (3309, 0.006272591746028671), (3310, 0.0), (3311, 0.0022941875363447282), (3312, 0.013575887940800117), (3313, 0.028787092659189734), (3314, 0.0026898098056917486), (3315, 0.03368318725728786), (3316, 0.007003850870270371), (3317, 0.011650735201311341), (3318, 0.012820183098572135), (3319, 0.02042323292226775), (3320, 0.0), (3321, 0.0), (3322, 0.0032640971868044587), (3323, 0.0), (3324, 0.0), (3325, 0.012773806745111468), (3326, 0.02913698815940024), (3327, 0.0022748666683518074), (3328, 0.03025804121512122), (3329, 0.008323855378347707), (3330, 0.033615999671213884), (3331, 0.005959816487740433), (3332, 0.0), (3333, 0.0), (3334, 0.0558349254710491), (3335, 0.0025624988480590443), (3336, 0.0022827623066486316), (3337, 0.002926360855104773), (3338, 0.004298076523995532), (3339, 0.003970201087966742), (3340, 0.0), (3341, 0.0025432834702508117), (3342, 0.006638970720780707), (3343, 0.0), (3344, 0.02738273881182292), (3345, 0.021626760319634532), (3346, 0.009080805971871126), (3347, 0.0021286521604270314), (3348, 0.002454413673103588), (3349, 0.007417544683405595), (3350, 0.0), (3351, 0.03422817266939724), (3352, 0.020253205328728124), (3353, 0.0026367027726778495), (3354, 0.0031930841877435712), (3355, 0.0029177922097563735), (3356, 0.013971822886881381), (3357, 0.0031524982659526623), (3358, 0.0030790201365820634), (3359, 0.0029515322197334465), (3360, 0.05160066999995516), (3361, 0.004367134773433362), (3362, 0.03655333120186724), (3363, 0.003163022311998248), (3364, 0.0029277933783362665), (3365, 0.0017885245766340776), (3366, 0.0), (3367, 0.004620646774560632), (3368, 0.0), (3369, 0.0023393798748198896), (3370, 0.01380740008929319), (3371, 0.0), (3372, 0.002663590840347564), (3373, 0.038926472514427574), (3374, 0.04659258370787397), (3375, 0.014880736050025874), (3376, 0.031092236059193583), (3377, 0.0316397347518423), (3378, 0.0), (3379, 0.0024864932425056924), (3380, 0.0022513613222782006), (3381, 0.002505897357895813), (3382, 0.01002898874098722), (3383, 0.0), (3384, 0.021404263877822273), (3385, 0.05898328865604495), (3386, 0.009225598651981193), (3387, 0.012348352343140651), (3388, 0.002672146305255844), (3389, 0.008373948421723199), (3390, 0.0024164444715753866), (3391, 0.005654239730508646), (3392, 0.001685166142478692), (3393, 0.0021812533691201504), (3394, 0.0), (3395, 0.048164788157745886), (3396, 0.002925354196686554), (3397, 0.0), (3398, 0.00475799272399742), (3399, 0.008506480833147213), (3400, 0.0), (3401, 0.0), (3402, 0.0024714558599442256), (3403, 0.018660913660548617), (3404, 0.00469377408637166), (3405, 0.003921088336881911), (3406, 0.0026765700485092483), (3407, 0.015189768722261746), (3408, 0.044040544320449265), (3409, 0.0380955187008168), (3410, 0.007326878072907434), (3411, 0.0), (3412, 0.002473500072167002), (3413, 0.0030462569383745484), (3414, 0.0028389857733314592), (3415, 0.0), (3416, 0.01824018993361663), (3417, 0.0027933086614350885), (3418, 0.008722324977241057), (3419, 0.002926833737465544), (3420, 0.02931512179853009), (3421, 0.014570533357246243), (3422, 0.0), (3423, 0.010418173494331847), (3424, 0.0), (3425, 0.002938660148668835), (3426, 0.010402151809410325), (3427, 0.041535867684028956), (3428, 0.024711329986341776), (3429, 0.0031366553343255815), (3430, 0.03306988583370248), (3431, 0.0020366287014385314), (3432, 0.00457959570783518), (3433, 0.021185525106043747), (3434, 0.0026981585993175548), (3435, 0.007080080814085195), (3436, 0.00719553939447874), (3437, 0.014891313208532216), (3438, 0.004925075352046846), (3439, 0.0), (3440, 0.005360191089565495), (3441, 0.0025153505923608713), (3442, 0.0), (3443, 0.004550394474658327), (3444, 0.0), (3445, 0.002597374923532215), (3446, 0.02376250738391038), (3447, 0.026998497642944902), (3448, 0.00559647446856459), (3449, 0.00274058636453638), (3450, 0.06274272831079739), (3451, 0.0049447961135720125), (3452, 0.006666829518739313), (3453, 0.007781907770548946), (3454, 0.0), (3455, 0.0023287089983759627), (3456, 0.007637110780276211), (3457, 0.007003019585887427), (3458, 0.006237886369444205), (3459, 0.0), (3460, 0.006574404057633163), (3461, 0.0), (3462, 0.057434079728437545), (3463, 0.060706045656025415), (3464, 0.00749830788075648), (3465, 0.07411089841255805), (3466, 0.032114814160377606), (3467, 0.0), (3468, 0.004972065267270442), (3469, 0.020745192410467787), (3470, 0.03501442704271948), (3471, 0.020413598846250346), (3472, 0.0), (3473, 0.0), (3474, 0.00649658195092293), (3475, 0.0), (3476, 0.0), (3477, 0.002514868609303398), (3478, 0.0025361871902406415), (3479, 0.0033870072429741257), (3480, 0.06560363079666712), (3481, 0.0), (3482, 0.0), (3483, 0.022015857129812924), (3484, 0.003836623982975266), (3485, 0.0), (3486, 0.03732961088277607), (3487, 0.0068740778119156035), (3488, 0.02758212253280522), (3489, 0.0), (3490, 0.0), (3491, 0.002546138032500976), (3492, 0.021034828753309146), (3493, 0.0026545144823408597), (3494, 0.0), (3495, 0.004102292524056775), (3496, 0.002722348105245073), (3497, 0.0027710447255302117), (3498, 0.036163887622597285), (3499, 0.007023650271851442), (3500, 0.002352966728399302), (3501, 0.007267483112732892), (3502, 0.0055839873596376976), (3503, 0.0024319481504375285), (3504, 0.019916439697188655), (3505, 0.0), (3506, 0.002925090773173954), (3507, 0.012116777808516594), (3508, 0.019891763683695312), (3509, 0.005699119019090606), (3510, 0.0), (3511, 0.037115909966507155), (3512, 0.003889013171202378), (3513, 0.004833569400596494), (3514, 0.007463910276476754), (3515, 0.007141768857087135), (3516, 0.007775657982650567), (3517, 0.0026259815785324952), (3518, 0.04319570152119698), (3519, 0.0), (3520, 0.00467025158615055), (3521, 0.008807933706918614), (3522, 0.0), (3523, 0.003635675158808224), (3524, 0.010712545862383618), (3525, 0.0), (3526, 0.002595503472085825), (3527, 0.0026216332494819416), (3528, 0.017064378305444217), (3529, 0.0), (3530, 0.0), (3531, 0.006862294924219214), (3532, 0.0), (3533, 0.0), (3534, 0.004188386236756716), (3535, 0.01384066315171278), (3536, 0.009447284878491278), (3537, 0.0031457463849610887), (3538, 0.0020222667751278976), (3539, 0.0), (3540, 0.0029580551139992647), (3541, 0.015766542718863782), (3542, 0.002594891823392815), (3543, 0.0), (3544, 0.0030871824814445417), (3545, 0.0), (3546, 0.0018921856768456724), (3547, 0.0), (3548, 0.0020856240241655002), (3549, 0.0), (3550, 0.0), (3551, 0.0025597255630833856), (3552, 0.04302665477519422), (3553, 0.020608214844184295), (3554, 0.0), (3555, 0.004471280542747129), (3556, 0.03384264898810406), (3557, 0.0024870467081049524), (3558, 0.014470291425645933), (3559, 0.04212369037310277), (3560, 0.0028496344498493186), (3561, 0.003438052370675986), (3562, 0.0), (3563, 0.0023114996233486447), (3564, 0.0025460210758847046), (3565, 0.002509988657408572), (3566, 0.006170320282172521), (3567, 0.0), (3568, 0.0), (3569, 0.002174456030263495), (3570, 0.007030792303727618), (3571, 0.007310855744198967), (3572, 0.029429181493142356), (3573, 0.02554701781763867), (3574, 0.027301137102037586), (3575, 0.0020489254243474405), (3576, 0.0046855570241939055), (3577, 0.003134300423040642), (3578, 0.0), (3579, 0.007771852322868443), (3580, 0.015039135519098676), (3581, 0.0), (3582, 0.011260065662471546), (3583, 0.004479553777020868), (3584, 0.00495460907849746), (3585, 0.0), (3586, 0.007614155228395089), (3587, 0.0028569324986325506), (3588, 0.005668212447753092), (3589, 0.0), (3590, 0.0026940584214214624), (3591, 0.0), (3592, 0.0), (3593, 0.0028311413543016003), (3594, 0.006542877340613763), (3595, 0.0), (3596, 0.009010933192656957), (3597, 0.03019147046334423), (3598, 0.0058148858738907615), (3599, 0.009506751045859305), (3600, 0.0), (3601, 0.002704796924602712), (3602, 0.004536165102704674), (3603, 0.0), (3604, 0.005067139324779593), (3605, 0.02727626839240265), (3606, 0.002585895851771812), (3607, 0.0), (3608, 0.0016519407502508059), (3609, 0.0), (3610, 0.0), (3611, 0.002881671319418458), (3612, 0.009614913459816828), (3613, 0.0031282114428502436), (3614, 0.002295596338649645), (3615, 0.002388296766524122), (3616, 0.003153843318530539), (3617, 0.0), (3618, 0.007578451625313122), (3619, 0.004047587780381726), (3620, 0.0030882893020226327), (3621, 0.0029843451284689345), (3622, 0.0), (3623, 0.007375385289240741), (3624, 0.00708332047076107), (3625, 0.0), (3626, 0.0019457778288461563), (3627, 0.002346613265148603), (3628, 0.0), (3629, 0.020937690266942786), (3630, 0.013248693386756738), (3631, 0.0), (3632, 0.006714251426310356), (3633, 0.0), (3634, 0.007698238156314156), (3635, 0.009666279084388135), (3636, 0.002613638129283211), (3637, 0.01243969337920028), (3638, 0.008913892551018446), (3639, 0.0029025843465260875), (3640, 0.015863756083686856), (3641, 0.0024493907161684263), (3642, 0.015425038196230128), (3643, 0.009249751025514882), (3644, 0.0), (3645, 0.00724440879850767), (3646, 0.002398125884687227), (3647, 0.0024952762541183417), (3648, 0.0067966355837907584), (3649, 0.0), (3650, 0.0), (3651, 0.002901290672648267), (3652, 0.037051038799886256), (3653, 0.007288033329822759), (3654, 0.002667297611504451), (3655, 0.0503792210482988), (3656, 0.03288836579668991), (3657, 0.0021402453501994092), (3658, 0.005945222312437101), (3659, 0.012739067427470985), (3660, 0.013717303640745986), (3661, 0.01564577425342385), (3662, 0.0), (3663, 0.0), (3664, 0.004434450523125298), (3665, 0.021010623387236353), (3666, 0.007423488483315582), (3667, 0.008900171105382566), (3668, 0.0021466768089874176), (3669, 0.00214929577871008), (3670, 0.014346236810449033), (3671, 0.0), (3672, 0.003603859110894286), (3673, 0.0025259098893481075), (3674, 0.009866519236776755), (3675, 0.016956370936491695), (3676, 0.0), (3677, 0.0027839214224453152), (3678, 0.0026980940701351206), (3679, 0.009695639399177612), (3680, 0.008084768946688057), (3681, 0.0), (3682, 0.0), (3683, 0.0), (3684, 0.02622063222790281), (3685, 0.0), (3686, 0.0), (3687, 0.0031677160464612685), (3688, 0.026503326352086173), (3689, 0.00941773693384183), (3690, 0.0), (3691, 0.0024132941512466618), (3692, 0.024225522273777434), (3693, 0.0), (3694, 0.015394318681617917), (3695, 0.0), (3696, 0.006894880242524032), (3697, 0.0), (3698, 0.0), (3699, 0.014528971303086509), (3700, 0.0), (3701, 0.02820311888611831), (3702, 0.0), (3703, 0.0), (3704, 0.007726207293318316), (3705, 0.006469532567629695), (3706, 0.0024751333238974306), (3707, 0.0025812562026774188), (3708, 0.013495528700764465), (3709, 0.0), (3710, 0.004904565905805378), (3711, 0.02491200660691427), (3712, 0.0), (3713, 0.015221954853509276), (3714, 0.002772130097690375), (3715, 0.0059530536022729275), (3716, 0.0), (3717, 0.0), (3718, 0.0), (3719, 0.0024754549920114216), (3720, 0.030103653738207493), (3721, 0.006120051103397477), (3722, 0.0), (3723, 0.004353829586358225), (3724, 0.0), (3725, 0.0023614834077740256), (3726, 0.0), (3727, 0.007088736271485593), (3728, 0.0563257370437377), (3729, 0.002939207932414357), (3730, 0.0), (3731, 0.03430420032682721), (3732, 0.0), (3733, 0.008671664222620296), (3734, 0.006743290499240995), (3735, 0.0), (3736, 0.0), (3737, 0.0028319594615577055), (3738, 0.0), (3739, 0.0025640637911042356), (3740, 0.0), (3741, 0.013577240544232178), (3742, 0.002316604456287793), (3743, 0.0), (3744, 0.005614568383030678), (3745, 0.002983416534820059), (3746, 0.024584595760600812), (3747, 0.011810499294329865), (3748, 0.005683490190282457), (3749, 0.002765280753409115), (3750, 0.012526912155733273), (3751, 0.02714324643460423), (3752, 0.00558054137277933), (3753, 0.04423112263249478), (3754, 0.00294123732407041), (3755, 0.002241461077547312), (3756, 0.011635471912017534), (3757, 0.0027358120658869957), (3758, 0.0), (3759, 0.0), (3760, 0.0), (3761, 0.0), (3762, 0.00330411757499818), (3763, 0.002988962008197595), (3764, 0.0), (3765, 0.0024636042749015424), (3766, 0.01696331878300543), (3767, 0.02842946435184831), (3768, 0.01255985800340293), (3769, 0.004823654473202804), (3770, 0.0026521310442793435), (3771, 0.007743879506289292), (3772, 0.0028861665077737704), (3773, 0.023394028419571652), (3774, 0.0049401024395021535), (3775, 0.010846868308484497), (3776, 0.00395109019216415), (3777, 0.015029275746340404), (3778, 0.021876216116220825), (3779, 0.10185805797079382), (3780, 0.007633761812979329), (3781, 0.0027174020257633258), (3782, 0.004941626446775452), (3783, 0.0), (3784, 0.008666453071715974), (3785, 0.0), (3786, 0.0), (3787, 0.005050684028750155), (3788, 0.004312418804018253), (3789, 0.0), (3790, 0.0), (3791, 0.0), (3792, 0.0025791715630782298), (3793, 0.044287917473408704), (3794, 0.011070808538151015), (3795, 0.0022686851808269076), (3796, 0.0), (3797, 0.01518071341031898), (3798, 0.0), (3799, 0.0024040976357289317), (3800, 0.0), (3801, 0.024514707385656417), (3802, 0.005051573170028611), (3803, 0.0), (3804, 0.002829137270933287), (3805, 0.0), (3806, 0.003891967785171729), (3807, 0.01415004543026814), (3808, 0.0), (3809, 0.002598493390633651), (3810, 0.023577201281668243), (3811, 0.0023908909837663888), (3812, 0.0), (3813, 0.002767235426300998), (3814, 0.029102136897891283), (3815, 0.004703487539245398), (3816, 0.0), (3817, 0.0), (3818, 0.0), (3819, 0.013430728987528886), (3820, 0.0), (3821, 0.007635870656724133), (3822, 0.010223324228813488), (3823, 0.004337632521968427), (3824, 0.004403203520833348), (3825, 0.005930841255515678), (3826, 0.00875332692435902), (3827, 0.002486666559187951), (3828, 0.017989862890400707), (3829, 0.008463648801411847), (3830, 0.0), (3831, 0.0), (3832, 0.003096146879951484), (3833, 0.004685092741441777), (3834, 0.0), (3835, 0.023973543229311105), (3836, 0.0), (3837, 0.0), (3838, 0.0), (3839, 0.022556611534142262), (3840, 0.0), (3841, 0.006411621947297271), (3842, 0.006439580046008823), (3843, 0.0), (3844, 0.005781129296899576), (3845, 0.00264536067742802), (3846, 0.0), (3847, 0.0), (3848, 0.0032176256582615117), (3849, 0.012140140403992342), (3850, 0.030492114933685623), (3851, 0.0), (3852, 0.02718070172661722), (3853, 0.01885012676492403), (3854, 0.06161566270378365), (3855, 0.002151981507583706), (3856, 0.0), (3857, 0.019866204573821197), (3858, 0.0), (3859, 0.0), (3860, 0.010597587690882967), (3861, 0.013592128894296429), (3862, 0.014856134944777388), (3863, 0.0022790086794717717), (3864, 0.006198950838403933), (3865, 0.005858147278425384), (3866, 0.0029234354102327348), (3867, 0.04005546355863066), (3868, 0.02332731372109037), (3869, 0.0), (3870, 0.0), (3871, 0.02774365781683594), (3872, 0.024065588995849797), (3873, 0.0027118935084019494), (3874, 0.0031013363262410347), (3875, 0.018078943775698533), (3876, 0.006562838398218208), (3877, 0.002823766391590152), (3878, 0.0033333249663985306), (3879, 0.0), (3880, 0.02973200671246554), (3881, 0.004399498239922743), (3882, 0.002669225472758663), (3883, 0.01621442671515648), (3884, 0.0029508011050974983), (3885, 0.0), (3886, 0.0044305555437740545), (3887, 0.0), (3888, 0.009509824437820174), (3889, 0.0027505286173344057), (3890, 0.0024536526556442157), (3891, 0.022651115487781825), (3892, 0.0032969468162486887), (3893, 0.0027398348303490174), (3894, 0.0022242858410916593), (3895, 0.01565752388060252), (3896, 0.0), (3897, 0.004891332365552052), (3898, 0.0024067454994173855), (3899, 0.007704160140244185), (3900, 0.002438771217157476), (3901, 0.008622386333348418), (3902, 0.0026388324543919197), (3903, 0.010429036686855615), (3904, 0.026076749500281174), (3905, 0.0074838650684981665), (3906, 0.002495287660533279), (3907, 0.004786368378027254), (3908, 0.004674093092431092), (3909, 0.006128669375239794), (3910, 0.006276866044991001), (3911, 0.00303052451245541), (3912, 0.0), (3913, 0.02250739185219301), (3914, 0.0), (3915, 0.0027547260209605175), (3916, 0.02128040043462383), (3917, 0.0024396790123713268), (3918, 0.0), (3919, 0.009518026688365582), (3920, 0.0026269850198830523), (3921, 0.0), (3922, 0.0031308493874409268), (3923, 0.020070827841297587), (3924, 0.010565245191918267), (3925, 0.0037750382833963), (3926, 0.006579383573264013), (3927, 0.020355178227915702), (3928, 0.002118505549736894), (3929, 0.0), (3930, 0.0), (3931, 0.0), (3932, 0.004678398488262888), (3933, 0.0), (3934, 0.019671452130892175), (3935, 0.0029885096547979943), (3936, 0.0), (3937, 0.0), (3938, 0.005002076654805726), (3939, 0.0033779025927503665), (3940, 0.00541580878603716), (3941, 0.009006728347892528), (3942, 0.005627567292449441), (3943, 0.0), (3944, 0.003718810489424915), (3945, 0.007385100505287984), (3946, 0.06577120166835922), (3947, 0.0387498132259521), (3948, 0.0), (3949, 0.009725553805078438), (3950, 0.0), (3951, 0.010623974779247279), (3952, 0.002908452739992948), (3953, 0.0023075672917894073), (3954, 0.008593121833034324), (3955, 0.0394911087324386), (3956, 0.00856647521911965), (3957, 0.01130737537328342), (3958, 0.013163592055294058), (3959, 0.02683911116641474), (3960, 0.008105392582227868), (3961, 0.03264324220881137), (3962, 0.002848391112204595), (3963, 0.024787115409651922), (3964, 0.0), (3965, 0.0), (3966, 0.004302620439293622), (3967, 0.0028036445992062004), (3968, 0.0), (3969, 0.0), (3970, 0.00441235901817224), (3971, 0.0), (3972, 0.0), (3973, 0.04191108684498302), (3974, 0.04564920918028945), (3975, 0.006013273983329386), (3976, 0.016645328263089863), (3977, 0.0), (3978, 0.02031608323873614), (3979, 0.0), (3980, 0.0), (3981, 0.0), (3982, 0.0), (3983, 0.0334519178853037), (3984, 0.010107881608489588), (3985, 0.0), (3986, 0.0022819497828374434), (3987, 0.0027012118924889077), (3988, 0.0), (3989, 0.0037165667421229062), (3990, 0.003500660434369241), (3991, 0.0), (3992, 0.01086432393823145), (3993, 0.010799299812975914), (3994, 0.0), (3995, 0.004783012688872665), (3996, 0.0), (3997, 0.00491138185917065), (3998, 0.0063284474489425134), (3999, 0.011834468356820938), (4000, 0.014109337523178098), (4001, 0.0065798866522937954), (4002, 0.0029453637825473953), (4003, 0.0), (4004, 0.029992838221305277), (4005, 0.03604246095974137), (4006, 0.0), (4007, 0.019400521420680113), (4008, 0.006817202182472819), (4009, 0.0060694965649699005), (4010, 0.0), (4011, 0.0023818585917991975), (4012, 0.017483243197010997), (4013, 0.007783966541683047), (4014, 0.0025661071943593977), (4015, 0.002092105915652035), (4016, 0.02100276004932242), (4017, 0.0034416299225726275), (4018, 0.0), (4019, 0.0032877144876280353), (4020, 0.0024881089755816052), (4021, 0.0), (4022, 0.0), (4023, 0.04164010241839035), (4024, 0.002738817823037397), (4025, 0.009445947734436947), (4026, 0.0), (4027, 0.0), (4028, 0.01865704422020719), (4029, 0.0), (4030, 0.0029685098507899778), (4031, 0.0), (4032, 0.01062426291591163), (4033, 0.010139571461229513), (4034, 0.0), (4035, 0.028844313228595903), (4036, 0.002478077422724702), (4037, 0.0), (4038, 0.007643493182656478), (4039, 0.004497181173511471), (4040, 0.0), (4041, 0.0), (4042, 0.0028011681307968453), (4043, 0.005142156064116709), (4044, 0.004185917988001526), (4045, 0.007474521320913149), (4046, 0.007837863472015384), (4047, 0.0058310531983781005), (4048, 0.010521792466705355), (4049, 0.002573949972108381), (4050, 0.022052871866018453), (4051, 0.0028294868139303216), (4052, 0.009622904531408717), (4053, 0.022649732315453208), (4054, 0.002689240504457996), (4055, 0.005924818293621736), (4056, 0.0025224767280474544), (4057, 0.005838723038181404), (4058, 0.0), (4059, 0.0023717520410445306), (4060, 0.009548933425246275), (4061, 0.007175096904403546), (4062, 0.05895899420588936), (4063, 0.0), (4064, 0.03630173900756346), (4065, 0.0), (4066, 0.002227252098130379), (4067, 0.0), (4068, 0.014451184354152647), (4069, 0.0024496794215734174), (4070, 0.0), (4071, 0.004365080839408345), (4072, 0.0), (4073, 0.0), (4074, 0.0022823850645029334), (4075, 0.002959310749705171), (4076, 0.004970043121679035), (4077, 0.007237935229267639), (4078, 0.0), (4079, 0.002629117011058859), (4080, 0.0022740107861656984), (4081, 0.017985275912985554), (4082, 0.00358280122205307), (4083, 0.002647802731253027), (4084, 0.0), (4085, 0.002413872752453439), (4086, 0.0), (4087, 0.002757014892292607), (4088, 0.019228802670990836), (4089, 0.007444294164478699), (4090, 0.00497122442224054), (4091, 0.005069099168848594), (4092, 0.008090895367233297), (4093, 0.0072372475745065045), (4094, 0.007582355866076667), (4095, 0.012071832731641165), (4096, 0.03176234276628577), (4097, 0.0), (4098, 0.007328628147016927), (4099, 0.006567093402415353), (4100, 0.0), (4101, 0.0027681114618960017), (4102, 0.0032201764133058803), (4103, 0.004638354930990023), (4104, 0.044651126235844864), (4105, 0.00794159514227583), (4106, 0.010011298899255085), (4107, 0.0031316484334973902), (4108, 0.0), (4109, 0.0), (4110, 0.005829926434041166), (4111, 0.0027150310497208023), (4112, 0.0), (4113, 0.0028169590729902245), (4114, 0.0), (4115, 0.0), (4116, 0.07264153003988619), (4117, 0.0028951057091739976), (4118, 0.007629579528410197), (4119, 0.005127533389383312), (4120, 0.005142394346497135), (4121, 0.013294058510116134), (4122, 0.008786711827347365), (4123, 0.05255262820554276), (4124, 0.01345966408865568), (4125, 0.0), (4126, 0.0029512048892630515), (4127, 0.0), (4128, 0.021763835526702892), (4129, 0.0024548456995279735), (4130, 0.0027720301380200125), (4131, 0.0), (4132, 0.002729915146874504), (4133, 0.0077958126868276235), (4134, 0.015345894727775013), (4135, 0.0025721544003564083), (4136, 0.002642025728427912), (4137, 0.06047703709769184), (4138, 0.002811175665091937), (4139, 0.0024490787046745617), (4140, 0.002771074176592469), (4141, 0.026591237443928675), (4142, 0.0032425169740557275), (4143, 0.0022797552107130963), (4144, 0.0), (4145, 0.0029791881546168577), (4146, 0.0), (4147, 0.0030881294441047137), (4148, 0.011642710729146653), (4149, 0.01872831087468419), (4150, 0.0), (4151, 0.004357507674573638), (4152, 0.03364084318782468), (4153, 0.0), (4154, 0.006460444818820417), (4155, 0.0024229225872662036), (4156, 0.01949743389303669), (4157, 0.0), (4158, 0.009601381761401219), (4159, 0.0), (4160, 0.027334340235441686), (4161, 0.0027284295702252356), (4162, 0.005309960252153657), (4163, 0.00828909244186234), (4164, 0.010674454149190896), (4165, 0.03529172143254559), (4166, 0.0), (4167, 0.0), (4168, 0.0), (4169, 0.0027015747367255603), (4170, 0.0), (4171, 0.0017924201375203218), (4172, 0.0033528725699006785), (4173, 0.0), (4174, 0.0023343493902812707), (4175, 0.029293305955632627), (4176, 0.020688748123160124), (4177, 0.02821768382122208), (4178, 0.014936139212549819), (4179, 0.0), (4180, 0.0), (4181, 0.0), (4182, 0.006907818896450108), (4183, 0.0024598501729012844), (4184, 0.007103928823641512), (4185, 0.0), (4186, 0.0), (4187, 0.010905512014133225), (4188, 0.0), (4189, 0.02126938217959492), (4190, 0.0), (4191, 0.0), (4192, 0.00930711991890133), (4193, 0.004195492760646212), (4194, 0.0), (4195, 0.03270387798303688), (4196, 0.007152503548435217), (4197, 0.0025854969931686654), (4198, 0.0), (4199, 0.0), (4200, 0.0020968865998536737), (4201, 0.0), (4202, 0.003546305715914872), (4203, 0.01875506443394477), (4204, 0.0), (4205, 0.00813259415956046), (4206, 0.0024090792775228152), (4207, 0.0), (4208, 0.005772631262084199), (4209, 0.03371052248760336), (4210, 0.00666279625006107), (4211, 0.004528622817440264), (4212, 0.0), (4213, 0.002411633257182007), (4214, 0.0), (4215, 0.0), (4216, 0.01129574202665622), (4217, 0.006344514387184781), (4218, 0.0), (4219, 0.0059307558518514976), (4220, 0.0022373580615292327), (4221, 0.003390872397994604), (4222, 0.0034013828055934094), (4223, 0.0), (4224, 0.0), (4225, 0.002662303167849778), (4226, 0.0071813010126941775), (4227, 0.012903133125254936), (4228, 0.002505610963151872), (4229, 0.0), (4230, 0.003249625623118119), (4231, 0.015173882829877295), (4232, 0.008355629863574444), (4233, 0.007493601501957861), (4234, 0.0), (4235, 0.010709589001293521), (4236, 0.00607498699543385), (4237, 0.0), (4238, 0.0), (4239, 0.0), (4240, 0.005036241334993982), (4241, 0.0), (4242, 0.026461169972595094), (4243, 0.0028872437447467303), (4244, 0.01629601541420167), (4245, 0.0027249016733194827), (4246, 0.015799090880616876), (4247, 0.0022291096577025686), (4248, 0.004586070327996085), (4249, 0.007376866463428255), (4250, 0.0), (4251, 0.004729825034580443), (4252, 0.06059815508412411), (4253, 0.0), (4254, 0.002381355869945804), (4255, 0.013906645140043448), (4256, 0.0), (4257, 0.008577179765386033), (4258, 0.0), (4259, 0.0028171123677211895), (4260, 0.0), (4261, 0.005249130933861092), (4262, 0.0026330476415983117), (4263, 0.0027933745595439814), (4264, 0.00454624722656051), (4265, 0.012370029362516657), (4266, 0.002559182443926289), (4267, 0.0029122220382451474), (4268, 0.04898548881218139), (4269, 0.0027203946975308474), (4270, 0.0), (4271, 0.0), (4272, 0.02992436166111102), (4273, 0.0025953107452440383), (4274, 0.004230225814165784), (4275, 0.004783375335158279), (4276, 0.0), (4277, 0.0023230286175405803), (4278, 0.0), (4279, 0.0), (4280, 0.0030057193500140156), (4281, 0.023073171694226444), (4282, 0.006581235977916588), (4283, 0.026170776624460865), (4284, 0.007015060521553908), (4285, 0.00541390337248493), (4286, 0.0026814309883877183), (4287, 0.0026201914461210334), (4288, 0.021746012783557665), (4289, 0.007530304372005355), (4290, 0.004163826251867192), (4291, 0.0), (4292, 0.004346641270334503), (4293, 0.01072496987906045), (4294, 0.02557831459377292), (4295, 0.0028956476258980364), (4296, 0.0022091218180194483), (4297, 0.0), (4298, 0.0031114236658140513), (4299, 0.006979491877667861), (4300, 0.0), (4301, 0.001881648020866405), (4302, 0.0), (4303, 0.006307820224547157), (4304, 0.0022762430833830217), (4305, 0.0), (4306, 0.0031355357755684875), (4307, 0.005179565875975142), (4308, 0.0027812821125682), (4309, 0.00697819374420941), (4310, 0.004618064119380746), (4311, 0.00206051039801924), (4312, 0.004956559811046084), (4313, 0.0), (4314, 0.01480113606160618), (4315, 0.0), (4316, 0.0), (4317, 0.0), (4318, 0.00267995282520947), (4319, 0.0), (4320, 0.0025297404552931534), (4321, 0.017028521917406638), (4322, 0.004224059410919858), (4323, 0.0), (4324, 0.0), (4325, 0.01084142860251558), (4326, 0.0023252246844545858), (4327, 0.0), (4328, 0.004309779076309047), (4329, 0.0), (4330, 0.00253759563114658), (4331, 0.005314131386390756), (4332, 0.0), (4333, 0.0028538356132755452), (4334, 0.0026212769553910806), (4335, 0.008058701805706186), (4336, 0.008794656199100885), (4337, 0.012416145648083689), (4338, 0.0), (4339, 0.004214172565029606), (4340, 0.0026230583862476183), (4341, 0.0), (4342, 0.006053130571462052), (4343, 0.002243294059099312), (4344, 0.011726694019006622), (4345, 0.0024056806139171995), (4346, 0.0), (4347, 0.0), (4348, 0.0023323300386728536), (4349, 0.01758778225581641), (4350, 0.0022859700538679396), (4351, 0.007044390945365722), (4352, 0.0), (4353, 0.0), (4354, 0.025503853369116335), (4355, 0.0027018875230114072), (4356, 0.002358670992777147), (4357, 0.0027034679302635803), (4358, 0.0), (4359, 0.002315457705635693), (4360, 0.004638002055274865), (4361, 0.0026386334816726476), (4362, 0.03662915792058017), (4363, 0.002656280498809686), (4364, 0.0), (4365, 0.004063496237183203), (4366, 0.010509642903648503), (4367, 0.00636561455566984), (4368, 0.002854344086319595), (4369, 0.0029178234754435894), (4370, 0.0), (4371, 0.009763787259413185), (4372, 0.0), (4373, 0.004944937742506397), (4374, 0.013502565967730251), (4375, 0.09117512301489193), (4376, 0.00472987449563689), (4377, 0.00473449738414215), (4378, 0.07894345402700793), (4379, 0.014738068688333519), (4380, 0.01909520187198896), (4381, 0.002458728622652153), (4382, 0.020364996372131905), (4383, 0.00462950343379809), (4384, 0.0048863605224429355), (4385, 0.005717363384544328), (4386, 0.00218734688146368), (4387, 0.013870068941198363), (4388, 0.006755130022591245), (4389, 0.059627372790876695), (4390, 0.00735207097581671), (4391, 0.002563059388397236), (4392, 0.0048578911171751425), (4393, 0.0), (4394, 0.002516685249546862), (4395, 0.02048882844913981), (4396, 0.036691969771720574), (4397, 0.0028225842511361253), (4398, 0.05848106495843603), (4399, 0.01690382353828356), (4400, 0.00323306097982072), (4401, 0.002833596125018068), (4402, 0.02872814853482014), (4403, 0.037695251803000804), (4404, 0.0), (4405, 0.0), (4406, 0.0), (4407, 0.003317390193547925), (4408, 0.0), (4409, 0.0025211780579558235), (4410, 0.0), (4411, 0.002172750642469467), (4412, 0.008375126016394905), (4413, 0.0), (4414, 0.0), (4415, 0.0), (4416, 0.0029853335777020916), (4417, 0.0), (4418, 0.003330912615368857), (4419, 0.0026439719893291574), (4420, 0.002674280774418094), (4421, 0.0), (4422, 0.0026208834421524514), (4423, 0.003288729379767851), (4424, 0.0), (4425, 0.0), (4426, 0.003980631223261024), (4427, 0.002533334775450861), (4428, 0.0024082352367095087), (4429, 0.002202062550120158), (4430, 0.007485544625895459), (4431, 0.007646034470317188), (4432, 0.006257829146207155), (4433, 0.0), (4434, 0.0), (4435, 0.009657090753751577), (4436, 0.019687104256688303), (4437, 0.0), (4438, 0.004422951263287813), (4439, 0.0), (4440, 0.01744862397356858), (4441, 0.004382409607814833), (4442, 0.009322506640795744), (4443, 0.035517277554201775), (4444, 0.009365545280548903), (4445, 0.001903935600604458), (4446, 0.002782149984041176), (4447, 0.0), (4448, 0.0026486240455653193), (4449, 0.0), (4450, 0.026782449810039397), (4451, 0.0), (4452, 0.037013130597535505), (4453, 0.0), (4454, 0.0), (4455, 0.0), (4456, 0.04486868834608456), (4457, 0.0), (4458, 0.003024789988948817), (4459, 0.006319462824825345), (4460, 0.0), (4461, 0.0024415519508728914), (4462, 0.005213474094856588), (4463, 0.0), (4464, 0.005865917370922849), (4465, 0.019123743707399048), (4466, 0.020787788619053546), (4467, 0.006785277754309836), (4468, 0.004028035082793067), (4469, 0.012008625600884141), (4470, 0.007371133673986452), (4471, 0.002689451482618859), (4472, 0.0024516055231321734), (4473, 0.0022088482857684994), (4474, 0.014977388808916114), (4475, 0.012791476247212132), (4476, 0.0021702148234961057), (4477, 0.011228675186954683), (4478, 0.0), (4479, 0.0023358563951205434), (4480, 0.0), (4481, 0.011167684757927798), (4482, 0.015224543828703422), (4483, 0.0), (4484, 0.0033814476312483683), (4485, 0.0), (4486, 0.014142096503967723), (4487, 0.002498674942563265), (4488, 0.039874200750535285), (4489, 0.0026898571212910427), (4490, 0.00847884672726767), (4491, 0.0), (4492, 0.019899656515150924), (4493, 0.0), (4494, 0.008076927428852684), (4495, 0.002716533945847962), (4496, 0.0), (4497, 0.0026552611205088346), (4498, 0.0), (4499, 0.0), (4500, 0.0), (4501, 0.0025623314809338042), (4502, 0.008778213671318655), (4503, 0.05019632180888005), (4504, 0.017262945955099827), (4505, 0.0026845407116629577), (4506, 0.0), (4507, 0.002913088748170219), (4508, 0.0), (4509, 0.0), (4510, 0.012406120488644513), (4511, 0.009055944146683143), (4512, 0.013096663788746788), (4513, 0.003816259526860173), (4514, 0.00558021931038109), (4515, 0.005133628241484277), (4516, 0.0029082392469185234), (4517, 0.007192818112932041), (4518, 0.0056003864349854155), (4519, 0.0), (4520, 0.00251065636202738), (4521, 0.0031656248700788828), (4522, 0.00779142357392963), (4523, 0.006839334010413386), (4524, 0.013344104735653138), (4525, 0.0), (4526, 0.0), (4527, 0.005304592026024582), (4528, 0.0027542947624417113), (4529, 0.0034005010522372646), (4530, 0.002480367673515684), (4531, 0.01576425025629922), (4532, 0.0), (4533, 0.03179699053985203), (4534, 0.022503792380745714), (4535, 0.0028386710230197294), (4536, 0.0024230497488252263), (4537, 0.006005299509575737), (4538, 0.028714680514426775), (4539, 0.0), (4540, 0.0027251255860746932), (4541, 0.0), (4542, 0.0), (4543, 0.011258339788766714), (4544, 0.003163843742069543), (4545, 0.0027445443902041006), (4546, 0.009241565345370469), (4547, 0.0), (4548, 0.026746394406841196), (4549, 0.0), (4550, 0.0024586748500938596), (4551, 0.010636691906109849), (4552, 0.004781914462610898), (4553, 0.010220370619708468), (4554, 0.02471715878629297), (4555, 0.003822393043576866), (4556, 0.0), (4557, 0.0075049104273801175), (4558, 0.0), (4559, 0.0), (4560, 0.0), (4561, 0.0), (4562, 0.0), (4563, 0.0026006699960084098), (4564, 0.006324868664687002), (4565, 0.0), (4566, 0.0026735546109579985), (4567, 0.0024239308498221444), (4568, 0.0), (4569, 0.0), (4570, 0.0), (4571, 0.00403004995905347), (4572, 0.0031126376024216505), (4573, 0.002458614741936614), (4574, 0.002715543513395254), (4575, 0.002683455745897461), (4576, 0.013324419282033591), (4577, 0.0), (4578, 0.0), (4579, 0.007706345424758964), (4580, 0.0), (4581, 0.007140956745791369), (4582, 0.004115089528140448), (4583, 0.0155091381014043), (4584, 0.0029816502268501864), (4585, 0.004316825219797294), (4586, 0.0048038743900341956), (4587, 0.004396915493480532), (4588, 0.040074741901526274), (4589, 0.002968495055423245), (4590, 0.030204049246894422), (4591, 0.006649489713339693), (4592, 0.0), (4593, 0.00795009926001135), (4594, 0.0624699521049894), (4595, 0.004991963728483643), (4596, 0.011579153357762677), (4597, 0.0), (4598, 0.001989708285475718), (4599, 0.0), (4600, 0.0), (4601, 0.007825524342012363), (4602, 0.03194663943884777), (4603, 0.008493147032227942), (4604, 0.0025498804584698246), (4605, 0.010113684386539628), (4606, 0.0032107990543004962), (4607, 0.003682819782953627), (4608, 0.02163472384787619), (4609, 0.0), (4610, 0.013579403390591703), (4611, 0.0033805137878272673), (4612, 0.008900541314353928), (4613, 0.0), (4614, 0.09362226751043302), (4615, 0.0), (4616, 0.0023428090596489324), (4617, 0.013145152122535166), (4618, 0.0), (4619, 0.01060441183101697), (4620, 0.00231727195620905), (4621, 0.004820847396153738), (4622, 0.0), (4623, 0.01164624107645406), (4624, 0.007497150714487852), (4625, 0.0026333505042846904), (4626, 0.002050481727273585), (4627, 0.015347594022472875), (4628, 0.0), (4629, 0.007458366306468024), (4630, 0.005173595112168345), (4631, 0.0), (4632, 0.0029900152728193187), (4633, 0.0029805712061734815), (4634, 0.002366537186237376), (4635, 0.0), (4636, 0.0021387597745254486), (4637, 0.01687894953209105), (4638, 0.0023135084446129625), (4639, 0.004827393660535323), (4640, 0.017919357514542884), (4641, 0.03444472756108918), (4642, 0.005444385938077968), (4643, 0.0026087964121890832), (4644, 0.0), (4645, 0.02833924807672003), (4646, 0.005882073074407983), (4647, 0.0), (4648, 0.0), (4649, 0.00836168035627167), (4650, 0.0029227923349272288), (4651, 0.0), (4652, 0.006959441062191511), (4653, 0.005640484385845355), (4654, 0.0), (4655, 0.0), (4656, 0.007629219763180771), (4657, 0.00272766942235733), (4658, 0.0199904648539231), (4659, 0.0235718202463927), (4660, 0.008816293072121558), (4661, 0.006337486653117293), (4662, 0.0), (4663, 0.03279450213536398), (4664, 0.008516099300011862), (4665, 0.004575605255719265), (4666, 0.00624575032328202), (4667, 0.0), (4668, 0.028690496767730313), (4669, 0.015492525466058645), (4670, 0.006848594424887118), (4671, 0.0), (4672, 0.0), (4673, 0.013777217612414589), (4674, 0.005742313437079809), (4675, 0.0), (4676, 0.0), (4677, 0.007226291498591362), (4678, 0.004715176978610753), (4679, 0.018725799861996212), (4680, 0.0027116711744928136), (4681, 0.0), (4682, 0.047558303125179786), (4683, 0.0), (4684, 0.027592473887778385), (4685, 0.008939084683528015), (4686, 0.002551643339660422), (4687, 0.0024798705471827), (4688, 0.0), (4689, 0.04291454282972678), (4690, 0.0), (4691, 0.006248887308908626), (4692, 0.0031658445386857584), (4693, 0.0024635743266324837), (4694, 0.0029799396515033144), (4695, 0.011784777485543659), (4696, 0.0033226057436817526), (4697, 0.004288320125964997), (4698, 0.005566055076203875), (4699, 0.008066732917858166), (4700, 0.0), (4701, 0.026815904466972303), (4702, 0.0), (4703, 0.03343412394967265), (4704, 0.003464734517458659), (4705, 0.0036260817428888804), (4706, 0.00281767098412393), (4707, 0.007924309197114073), (4708, 0.004578152801117167), (4709, 0.015887549483793922), (4710, 0.00903722525774957), (4711, 0.0), (4712, 0.0022846896996839036), (4713, 0.0029359206463355366), (4714, 0.0), (4715, 0.007168016491301172), (4716, 0.0), (4717, 0.0029946805054474088), (4718, 0.002844408783172781), (4719, 0.004912020457018882), (4720, 0.0), (4721, 0.03551125010985394), (4722, 0.0180897110972239), (4723, 0.00310090615463497), (4724, 0.0470198964390734), (4725, 0.0), (4726, 0.005357462984646266), (4727, 0.031066252344282376), (4728, 0.0), (4729, 0.0024361362289319404), (4730, 0.0), (4731, 0.025474366897877264), (4732, 0.0027662301144192277), (4733, 0.005965512302462513), (4734, 0.0027408297226725643), (4735, 0.016832454872681257), (4736, 0.0), (4737, 0.0), (4738, 0.0065658473500210725), (4739, 0.032994541915988086), (4740, 0.0), (4741, 0.0), (4742, 0.0), (4743, 0.002474603104085691), (4744, 0.002055966077073321), (4745, 0.0), (4746, 0.00523258618884702), (4747, 0.013451885684782254), (4748, 0.007885550521461237), (4749, 0.0034036456368132157), (4750, 0.0), (4751, 0.0), (4752, 0.0018166836686154622), (4753, 0.0028919487884017663), (4754, 0.0), (4755, 0.0), (4756, 0.002632461050300673), (4757, 0.00750809522210286), (4758, 0.0), (4759, 0.0)]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "len(Recommendation_Score)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hQcgGipTQ5bb",
        "outputId": "cb3b1986-af1b-4105-a8b5-c435ac04738c"
      },
      "execution_count": 114,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "4760"
            ]
          },
          "metadata": {},
          "execution_count": 114
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Get All Movies Sort Based on Recommendation Score wrt Favourite Movie"
      ],
      "metadata": {
        "id": "B5NbFNVWVDXj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "Sorted_Similar_Movies = sorted(Recommendation_Score, key = lambda x:x[1], reverse = True)\n",
        "print(Sorted_Similar_Movies)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jwbMQU8pQ9hI",
        "outputId": "81235618-2fea-4e09-d2cb-e9e226ead068"
      },
      "execution_count": 115,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[(2692, 1.0000000000000002), (3276, 0.11904275527845871), (3779, 0.10185805797079382), (62, 0.10153560702418994), (2903, 0.10063787314386034), (1647, 0.09397055536069451), (4614, 0.09362226751043302), (4375, 0.09117512301489193), (45, 0.08999324643162435), (1383, 0.08425242441722802), (110, 0.08361784775029485), (628, 0.08334515876919323), (1994, 0.08287835345252216), (2558, 0.08267633224298852), (1070, 0.08104448918225104), (4378, 0.07894345402700793), (1341, 0.07732693809361939), (1977, 0.07510309168081497), (3465, 0.07411089841255805), (3053, 0.0732438108456325), (4116, 0.07264153003988619), (1982, 0.07246569778553744), (2538, 0.06802035746289192), (3248, 0.06683400770968473), (3946, 0.06577120166835922), (3480, 0.06560363079666712), (254, 0.06351452702158421), (590, 0.06275727122098754), (3450, 0.06274272831079739), (1886, 0.06267985852941994), (4594, 0.0624699521049894), (2112, 0.06218435141221765), (84, 0.0618237599684129), (675, 0.06176991517572303), (3854, 0.06161566270378365), (1134, 0.06151448371353247), (3463, 0.060706045656025415), (4252, 0.06059815508412411), (4137, 0.06047703709769184), (1118, 0.05998954734066491), (4389, 0.059627372790876695), (3385, 0.05898328865604495), (4062, 0.05895899420588936), (282, 0.05879285017883316), (4398, 0.05848106495843603), (424, 0.05839654732699123), (2358, 0.05826769637272555), (3462, 0.057434079728437545), (2985, 0.05717355295839895), (2318, 0.05698746413620388), (1021, 0.05671999964768967), (3728, 0.0563257370437377), (3334, 0.0558349254710491), (1243, 0.05520158300072489), (1970, 0.05299390678023471), (2026, 0.05264268750759823), (4123, 0.05255262820554276), (137, 0.052487743978234754), (3360, 0.05160066999995516), (877, 0.0512230973907653), (292, 0.05110461872364794), (761, 0.050844325355354554), (873, 0.05064812913191185), (1030, 0.050582789674035046), (2191, 0.050557727650637894), (2944, 0.050454430002777675), (3655, 0.0503792210482988), (1148, 0.05022542698748972), (4503, 0.05019632180888005), (1102, 0.05016977076463526), (479, 0.04998855981862962), (3203, 0.0498349227897459), (1809, 0.049588147032597375), (213, 0.049335863613711506), (227, 0.049272711641777656), (519, 0.04913582561387614), (4268, 0.04898548881218139), (2630, 0.04898534827274639), (2417, 0.048975289561833585), (2133, 0.04895833694100604), (384, 0.048561612573761986), (2214, 0.04836649295986437), (2550, 0.04836540834452215), (2579, 0.048167961252127585), (3395, 0.048164788157745886), (1878, 0.048053795166414184), (2294, 0.04801663260090347), (3010, 0.0475919192650606), (4682, 0.047558303125179786), (2374, 0.047351480752962534), (4724, 0.0470198964390734), (2653, 0.04697351928240422), (3374, 0.04659258370787397), (3294, 0.04624323347380142), (1023, 0.04614573925419343), (3974, 0.04564920918028945), (67, 0.04506617878405939), (412, 0.04506044778254056), (904, 0.045049265599229504), (3091, 0.04501840790205196), (2151, 0.04489615902161054), (4456, 0.04486868834608456), (2530, 0.04481510146028207), (4104, 0.044651126235844864), (1257, 0.04460086738980612), (1261, 0.044570869220417475), (1302, 0.044531189691413835), (3023, 0.04447257244459566), (3793, 0.044287917473408704), (3753, 0.04423112263249478), (637, 0.044214370060605246), (2971, 0.044168735616715235), (3408, 0.044040544320449265), (328, 0.043787258882396256), (2694, 0.04368554902472678), (1292, 0.04367380160992527), (615, 0.043627287472934005), (1821, 0.04361028830378264), (161, 0.04350231968158566), (1203, 0.043288373397248), (2745, 0.04326153862816202), (3518, 0.04319570152119698), (2893, 0.043187343639666156), (1248, 0.04316322790320628), (438, 0.04307224044369871), (277, 0.04305955678902839), (682, 0.043040904339148985), (3552, 0.04302665477519422), (2012, 0.04293853193777039), (4689, 0.04291454282972678), (673, 0.04277602512082654), (408, 0.04269519176334115), (1506, 0.042282530621225375), (455, 0.04213396440391408), (3559, 0.04212369037310277), (3973, 0.04191108684498302), (1358, 0.0418305667382064), (1393, 0.041789154386127465), (172, 0.041690425384126525), (4023, 0.04164010241839035), (3427, 0.041535867684028956), (1850, 0.04146507077720888), (2248, 0.04144905622988321), (360, 0.04140490881144238), (1871, 0.04119734499545335), (1713, 0.041056464531435785), (3249, 0.04101786522213684), (2321, 0.04096332211047457), (2869, 0.040554179176207086), (3209, 0.0404720498947614), (1675, 0.040396587516422805), (2846, 0.04034937166874806), (1369, 0.04027355663153479), (89, 0.04014807769109404), (4588, 0.040074741901526274), (3867, 0.04005546355863066), (2155, 0.04005254584556308), (4488, 0.039874200750535285), (2295, 0.03982190635490875), (185, 0.03981648215324947), (1320, 0.0397552488399696), (44, 0.03961780430399104), (3955, 0.0394911087324386), (1527, 0.03945167296049171), (3373, 0.038926472514427574), (2859, 0.03892062672772363), (210, 0.038872494075225), (1652, 0.03875069306724735), (3947, 0.0387498132259521), (108, 0.03871190052571693), (632, 0.03852152259053765), (109, 0.038488255428289986), (3409, 0.0380955187008168), (126, 0.03803411394029396), (2308, 0.03786870914432212), (4403, 0.037695251803000804), (2187, 0.03763919382653321), (2622, 0.03748821698202329), (3486, 0.03732961088277607), (2540, 0.037262447116274064), (3511, 0.037115909966507155), (1024, 0.037086309751285476), (3652, 0.037051038799886256), (4452, 0.037013130597535505), (788, 0.036775782506030336), (1676, 0.03676900030404152), (4396, 0.036691969771720574), (4362, 0.03662915792058017), (3127, 0.036590721490267514), (3362, 0.03655333120186724), (774, 0.03653446982082753), (3280, 0.03633050021075282), (4064, 0.03630173900756346), (1085, 0.036238762035520095), (3498, 0.036163887622597285), (2212, 0.036114079291876294), (2316, 0.03605001327712352), (4005, 0.03604246095974137), (2716, 0.03603309472599682), (2375, 0.036029161296792664), (911, 0.03585824955577745), (710, 0.03578166731017038), (2018, 0.03563383095352764), (4443, 0.035517277554201775), (4721, 0.03551125010985394), (874, 0.03549031987804057), (2371, 0.03544860769227722), (1991, 0.035376604288887115), (4165, 0.03529172143254559), (1241, 0.035270697376675486), (694, 0.035178367818131856), (3470, 0.03501442704271948), (3045, 0.03500487119962276), (1272, 0.034794423140693004), (2908, 0.03473069779062641), (2868, 0.03471057850484338), (3102, 0.03452469488743669), (830, 0.03447452468561071), (540, 0.03445972856479224), (1389, 0.03445912028134007), (4641, 0.03444472756108918), (2981, 0.03442583219886153), (818, 0.03439755809850987), (2109, 0.03435264766714195), (3731, 0.03430420032682721), (3351, 0.03422817266939724), (1568, 0.03407235441443471), (1379, 0.03405703604165394), (1702, 0.03401178055455821), (1311, 0.03394663995212679), (2123, 0.03394554340436231), (3255, 0.033861184392018406), (3556, 0.03384264898810406), (4209, 0.03371052248760336), (3315, 0.03368318725728786), (4152, 0.03364084318782468), (3330, 0.033615999671213884), (3983, 0.0334519178853037), (4703, 0.03343412394967265), (721, 0.03336245332783653), (1236, 0.03334196963686731), (1752, 0.03333938657742233), (578, 0.03327816265992636), (2122, 0.03310797958980469), (334, 0.033097160057045466), (3430, 0.03306988583370248), (1367, 0.03305734622286169), (4739, 0.032994541915988086), (3656, 0.03288836579668991), (4663, 0.03279450213536398), (3137, 0.03279268523839364), (1770, 0.03278254752073779), (4195, 0.03270387798303688), (3961, 0.03264324220881137), (3004, 0.032584681512207773), (387, 0.032522091160063736), (2365, 0.03251802786423902), (2476, 0.03244347050543419), (1464, 0.03242600299745582), (1837, 0.03240258300693197), (1063, 0.0323986861553641), (166, 0.03236744328857419), (462, 0.03225758483924034), (138, 0.032196594696629596), (2147, 0.032118367696370734), (3466, 0.032114814160377606), (935, 0.0320740971372626), (547, 0.03205811100816747), (4602, 0.03194663943884777), (1146, 0.03193270995829649), (2751, 0.03186976241331189), (864, 0.031860195855372704), (4533, 0.03179699053985203), (4096, 0.03176234276628577), (823, 0.03170971693957012), (65, 0.031680929113056686), (3377, 0.0316397347518423), (1195, 0.03160288863475456), (2517, 0.031513234738017475), (2100, 0.031466640098441356), (2621, 0.031445444080265395), (2082, 0.03137256966163152), (812, 0.03134464238097974), (3376, 0.031092236059193583), (1068, 0.031080086209754408), (4727, 0.031066252344282376), (1885, 0.0309975246079396), (1499, 0.030795662279307377), (3157, 0.030753179174541134), (179, 0.030707903325990372), (1868, 0.030647250708224397), (174, 0.030569480499441422), (3850, 0.030492114933685623), (1173, 0.030413463227986912), (1750, 0.030273505619146518), (3328, 0.03025804121512122), (787, 0.030234382676036564), (4590, 0.030204049246894422), (1043, 0.03019341492590413), (3597, 0.03019147046334423), (2023, 0.030168509278277092), (2807, 0.030117994968785384), (3720, 0.030103653738207493), (2014, 0.030095920732595108), (4004, 0.029992838221305277), (2413, 0.029928886003016544), (4272, 0.02992436166111102), (2710, 0.02988730591823796), (2037, 0.0298193260783485), (2443, 0.029803434615890047), (618, 0.029763727969072954), (530, 0.02974102103303271), (3880, 0.02973200671246554), (250, 0.029605156266211453), (3146, 0.02959142995417388), (1795, 0.029589075994988966), (1648, 0.029561843201275848), (1976, 0.029555193895324648), (2114, 0.029513454653019616), (2887, 0.029503613070800693), (2782, 0.029448976097656177), (3572, 0.029429181493142356), (2706, 0.029422744288845587), (3420, 0.02931512179853009), (4175, 0.029293305955632627), (2614, 0.029225820521244943), (193, 0.029212491040047014), (1973, 0.02915657413264359), (3326, 0.02913698815940024), (3814, 0.029102136897891283), (1788, 0.029045998553708444), (952, 0.029031084004495476), (629, 0.0290204466032395), (4035, 0.028844313228595903), (3313, 0.028787092659189734), (1046, 0.028771864585929827), (1405, 0.028769066044756323), (4402, 0.02872814853482014), (1363, 0.028717455504198453), (4538, 0.028714680514426775), (4668, 0.028690496767730313), (766, 0.02863597006015581), (1482, 0.028603312957890946), (976, 0.028498609827027066), (2481, 0.02847926123774087), (430, 0.028474447896110415), (112, 0.028472602360715568), (2198, 0.028466562898500053), (2102, 0.028465544090018308), (241, 0.02846230566947309), (2221, 0.028430482696010374), (3767, 0.02842946435184831), (1990, 0.0284201409286951), (2723, 0.02837260039695167), (693, 0.028339830117329528), (4645, 0.02833924807672003), (465, 0.02832340194230098), (371, 0.028251554740421535), (1398, 0.028222452550706812), (4177, 0.02821768382122208), (3701, 0.02820311888611831), (2487, 0.0281679357752627), (836, 0.028164079074357654), (1560, 0.028142719658602232), (428, 0.027941476362352217), (2876, 0.02775849524463103), (3871, 0.02774365781683594), (670, 0.027728288572825423), (2791, 0.027708494673946583), (2343, 0.02760157045044117), (4684, 0.027592473887778385), (3488, 0.02758212253280522), (1137, 0.027530878040813937), (421, 0.02749177219642947), (3174, 0.02743679517966769), (3344, 0.02738273881182292), (4160, 0.027334340235441686), (3574, 0.027301137102037586), (1500, 0.02729943310930179), (903, 0.0272937967913948), (3605, 0.02727626839240265), (1845, 0.02726613451399632), (1634, 0.027265975858920755), (1095, 0.027246132772978986), (284, 0.027210766517313724), (176, 0.027183803724459624), (3852, 0.02718070172661722), (3751, 0.02714324643460423), (1162, 0.027084968030862168), (3447, 0.026998497642944902), (593, 0.0269834518549629), (2802, 0.02690014016428078), (3959, 0.02683911116641474), (4701, 0.026815904466972303), (4450, 0.026782449810039397), (4548, 0.026746394406841196), (522, 0.026704190546478417), (2920, 0.02664140279351682), (2912, 0.026637958351887214), (2154, 0.026634248456284985), (1314, 0.026598285558358734), (4141, 0.026591237443928675), (3028, 0.026584450169584505), (167, 0.026576509643169363), (1205, 0.026572826699719294), (1430, 0.02653057804103264), (3688, 0.026503326352086173), (1720, 0.026475090126577592), (4242, 0.026461169972595094), (1847, 0.026430755901808753), (240, 0.02640964525511218), (852, 0.026315624754250793), (2013, 0.02631318545102932), (3684, 0.02622063222790281), (1059, 0.026187328256908955), (4283, 0.026170776624460865), (832, 0.02610503660845372), (381, 0.02609320340969504), (3904, 0.026076749500281174), (3167, 0.026076234240691325), (3154, 0.02606963846967903), (459, 0.026041390263338297), (2687, 0.026027725036469426), (2276, 0.02602103823289531), (2762, 0.025980223803704138), (3260, 0.025956117613509078), (3017, 0.025952831108870544), (2972, 0.025931096430882088), (2394, 0.02568905521652685), (25, 0.025600660315408176), (4294, 0.02557831459377292), (3573, 0.02554701781763867), (1721, 0.025534461225381583), (1060, 0.025524774616417), (2467, 0.02552401265792079), (4354, 0.025503853369116335), (3156, 0.025482070893600085), (4731, 0.025474366897877264), (2011, 0.025123628978433857), (2094, 0.02510748187337649), (2048, 0.025093016553148453), (2761, 0.025056785877878327), (3285, 0.024986270155456007), (124, 0.024984856011144883), (1763, 0.024934636005999537), (3711, 0.02491200660691427), (1181, 0.02490892907408937), (1351, 0.024875575685802023), (967, 0.02484089246980712), (1749, 0.024814387662836442), (345, 0.024810895755894055), (3963, 0.024787115409651922), (1572, 0.02474448545068361), (2408, 0.024729842506337994), (269, 0.024722211015322175), (4554, 0.02471715878629297), (3428, 0.024711329986341776), (1999, 0.024674542916240657), (3746, 0.024584595760600812), (1544, 0.02457419064673378), (824, 0.02455387204481398), (657, 0.02453562880347747), (2689, 0.024527497165292594), (3801, 0.024514707385656417), (2020, 0.024235620690403414), (116, 0.02423134884513523), (1530, 0.02423044829538496), (3692, 0.024225522273777434), (2560, 0.024171741903165515), (3872, 0.024065588995849797), (942, 0.02404326236955836), (2173, 0.02400710912107853), (3835, 0.023973543229311105), (2484, 0.02391517705724991), (3446, 0.02376250738391038), (2950, 0.023732959516752646), (885, 0.02372906869332012), (1412, 0.023629897886256662), (2638, 0.023625589296039667), (3810, 0.023577201281668243), (4659, 0.0235718202463927), (2649, 0.0235700589676888), (155, 0.023537765450918877), (1057, 0.02343832337120043), (2713, 0.023432161916103617), (3773, 0.023394028419571652), (1283, 0.023375973429109315), (175, 0.023330531483932517), (3868, 0.02332731372109037), (2699, 0.02329919140759537), (1865, 0.0232913893449777), (29, 0.023288277583204436), (1186, 0.023229264871711574), (2718, 0.02319674459478677), (3153, 0.023168777515517318), (1997, 0.023141379590983783), (4281, 0.023073171694226444), (2040, 0.022971868335819254), (1585, 0.02294775132215635), (706, 0.02288398192631816), (2647, 0.02278830310814006), (1935, 0.022777338759990606), (3891, 0.022651115487781825), (4053, 0.022649732315453208), (68, 0.022589410734540884), (3839, 0.022556611534142262), (15, 0.022556564866386044), (3913, 0.02250739185219301), (4534, 0.022503792380745714), (515, 0.022499833096115873), (1362, 0.022486463991498958), (1015, 0.022477148208897783), (691, 0.022330801569338962), (3095, 0.02232378376646734), (261, 0.02232369294417245), (88, 0.022301178722772527), (2157, 0.02224516374878037), (1996, 0.0222321859914211), (1141, 0.022221388090035325), (2096, 0.022163124512581702), (641, 0.022162243129839825), (613, 0.02210391733671185), (1515, 0.022061747166271108), (4050, 0.022052871866018453), (3483, 0.022015857129812924), (398, 0.02199549736073778), (2449, 0.021985066932388473), (1505, 0.021982373147284715), (3778, 0.021876216116220825), (917, 0.021822162443509208), (257, 0.021804620814370096), (4128, 0.021763835526702892), (4288, 0.021746012783557665), (672, 0.021739478274217176), (1492, 0.02171558070297426), (2210, 0.021656005592106047), (4608, 0.02163472384787619), (3345, 0.021626760319634532), (1707, 0.021603149809261358), (2822, 0.0215532629683982), (1757, 0.021518240078453512), (2777, 0.02151782398151878), (1629, 0.021463985617207366), (3384, 0.021404263877822273), (2668, 0.021394926823283075), (2646, 0.021358135818460758), (1861, 0.02132668519986058), (1033, 0.02132016719433776), (442, 0.021288297567688543), (2598, 0.021287142760911603), (3916, 0.02128040043462383), (4189, 0.02126938217959492), (3068, 0.021254290997707096), (1270, 0.021212009876187383), (3433, 0.021185525106043747), (1942, 0.02115515210916598), (1397, 0.021082777924745753), (3492, 0.021034828753309146), (1985, 0.021011193896198634), (3665, 0.021010623387236353), (4016, 0.02100276004932242), (3629, 0.020937690266942786), (3222, 0.02092202862294061), (1385, 0.020819608375770078), (4466, 0.020787788619053546), (1817, 0.020764535380750283), (3469, 0.020745192410467787), (2440, 0.020740361118753315), (763, 0.02069291081637438), (4176, 0.020688748123160124), (1678, 0.020674657614782856), (1671, 0.020621715808903353), (2055, 0.020617915628473392), (2174, 0.02061080199928024), (3553, 0.020608214844184295), (4395, 0.02048882844913981), (1510, 0.020480695787819872), (3319, 0.02042323292226775), (3471, 0.020413598846250346), (1003, 0.02040558863047458), (4382, 0.020364996372131905), (3927, 0.020355178227915702), (2301, 0.020346391053315458), (870, 0.020332227193004895), (3978, 0.02031608323873614), (3083, 0.020305822398005775), (1471, 0.020290800155578558), (3352, 0.020253205328728124), (1132, 0.020242473075204687), (2768, 0.02022019513311771), (1017, 0.020210828878643068), (643, 0.02014941724072286), (2808, 0.020148475915238922), (2582, 0.020104138588029275), (3923, 0.020070827841297587), (2501, 0.020059505094761957), (2524, 0.020004759477924062), (4658, 0.0199904648539231), (2995, 0.01996032958314584), (1838, 0.019939936935035117), (3254, 0.019934000066389027), (3504, 0.019916439697188655), (330, 0.01990757698892509), (4492, 0.019899656515150924), (3508, 0.019891763683695312), (1098, 0.01988028147728714), (3857, 0.019866204573821197), (779, 0.019778519028090427), (1657, 0.019728179313836136), (2841, 0.01969468096073799), (4436, 0.019687104256688303), (329, 0.019680187212331626), (3934, 0.019671452130892175), (1927, 0.019666945381093325), (2867, 0.019569346792707398), (1052, 0.01949757886898508), (4156, 0.01949743389303669), (383, 0.019467817150654654), (4007, 0.019400521420680113), (2362, 0.019305653311181028), (463, 0.019270774055312006), (142, 0.01924033807026037), (4088, 0.019228802670990836), (947, 0.01918803569573748), (2469, 0.019146859249126912), (669, 0.01913232163764439), (145, 0.019128060100674707), (4465, 0.019123743707399048), (4380, 0.01909520187198896), (566, 0.019085435302379772), (1202, 0.019084727907330734), (2767, 0.019020439331965698), (2618, 0.01901317620959763), (2736, 0.01900887034546454), (199, 0.018959792932713843), (768, 0.01889780127429161), (3853, 0.01885012676492403), (3111, 0.018849760702424365), (1386, 0.01883315792718334), (2932, 0.018807248735502158), (4203, 0.01875506443394477), (4149, 0.01872831087468419), (4679, 0.018725799861996212), (2760, 0.018712458702392774), (204, 0.018686269670332167), (553, 0.018685764365025583), (3144, 0.01868398340994474), (3403, 0.018660913660548617), (4028, 0.01865704422020719), (2607, 0.01863811941695475), (33, 0.018612326068635436), (2650, 0.018583354119550942), (3284, 0.018580379689813888), (46, 0.01855499596172605), (83, 0.018501078945740605), (2237, 0.018480469432030938), (1937, 0.01843060245413057), (3097, 0.018399578507274313), (968, 0.018377219999664365), (1443, 0.01831419707001223), (1074, 0.018313355636506795), (3000, 0.018313196560767752), (2645, 0.01830642082683205), (160, 0.018298437262288456), (2368, 0.018295323351875652), (2513, 0.018276897871510427), (123, 0.018256088885426403), (3416, 0.01824018993361663), (689, 0.01823124484931015), (757, 0.018171478905814088), (364, 0.018118667495208754), (1872, 0.01809054728158338), (4722, 0.0180897110972239), (3875, 0.018078943775698533), (1226, 0.018073460855467367), (1175, 0.01805082944164325), (3828, 0.017989862890400707), (147, 0.01798970888682872), (4081, 0.017985275912985554), (2795, 0.017963854794401393), (4640, 0.017919357514542884), (808, 0.01788485830207994), (858, 0.01786248303974472), (222, 0.017856013028360415), (2035, 0.017841694875906363), (1112, 0.017814761595896286), (2167, 0.01780073194851991), (2070, 0.017785602537673223), (1365, 0.017784588946112626), (1843, 0.01777743540800436), (1384, 0.017767725898371563), (1129, 0.017757748873229732), (61, 0.017658795452635247), (342, 0.017625924860547256), (1274, 0.01759247947637767), (4349, 0.01758778225581641), (2823, 0.01753869196282759), (106, 0.017511756601740806), (796, 0.01748508210449308), (4012, 0.017483243197010997), (4440, 0.01744862397356858), (3085, 0.017441414767477733), (2553, 0.01743749009788074), (1579, 0.017412512530218235), (2093, 0.017353497854371687), (144, 0.017350164505517556), (1245, 0.01733780597970789), (4504, 0.017262945955099827), (1064, 0.01723362178999547), (3129, 0.01715175212683575), (1493, 0.017113614659723917), (3279, 0.01710645888961131), (1403, 0.017089358343226592), (3528, 0.017064378305444217), (409, 0.017054864370849368), (4321, 0.017028521917406638), (3036, 0.01700523802225701), (3766, 0.01696331878300543), (2207, 0.016959411662291247), (173, 0.01695754465504918), (3675, 0.016956370936491695), (2742, 0.0169510462112069), (794, 0.016938690601848962), (2119, 0.016936626721809577), (203, 0.01692391575379628), (916, 0.016917139639294917), (776, 0.016907533747342923), (4399, 0.01690382353828356), (1759, 0.016900019192624616), (2654, 0.016882448039672114), (4637, 0.01687894953209105), (4735, 0.016832454872681257), (3098, 0.01682852088519415), (677, 0.01682247009934885), (1377, 0.016773445546711195), (2110, 0.01675128583620694), (3226, 0.016748323767747708), (2712, 0.016746711251381167), (279, 0.01674439634537899), (212, 0.01673880855230024), (3213, 0.016734398067455605), (795, 0.016724564291810132), (2149, 0.016711990529519685), (2406, 0.016708556127859726), (3228, 0.01664828857203829), (3976, 0.016645328263089863), (2258, 0.016645098924895147), (3275, 0.016625701732328566), (937, 0.01661899895760169), (433, 0.016594829303328437), (3019, 0.016559249698570755), (2161, 0.01649460634120045), (638, 0.01648509407336536), (860, 0.016481212100768684), (2347, 0.016442297909857247), (1275, 0.016413131014958164), (1609, 0.01638052278217861), (218, 0.016329345660994338), (209, 0.016326637209159098), (4244, 0.01629601541420167), (551, 0.016277960178301926), (876, 0.016236183953495645), (1417, 0.016231265772845838), (1184, 0.016227879133609922), (1216, 0.016219260534941972), (3883, 0.01621442671515648), (511, 0.016166552419491664), (280, 0.016137762281668154), (3043, 0.016102860661864705), (853, 0.01607702326648414), (1254, 0.016063876077209334), (1445, 0.01603828875201241), (533, 0.015999131525746606), (586, 0.015989792128490082), (2917, 0.01597938404955991), (1716, 0.015952807160996087), (3012, 0.015947957006243817), (1018, 0.015920831393077692), (4709, 0.015887549483793922), (701, 0.015878620948365185), (1774, 0.015876691830685904), (458, 0.015871922723417135), (3640, 0.015863756083686856), (2275, 0.015828663325572444), (1523, 0.015826030293870766), (2353, 0.015804215693918204), (4246, 0.015799090880616876), (343, 0.015792700017701194), (692, 0.01577967045091189), (3541, 0.015766542718863782), (888, 0.015765180129318643), (4531, 0.01576425025629922), (1045, 0.01574002225933099), (48, 0.015673410180680997), (2290, 0.015664174994228695), (3895, 0.01565752388060252), (2996, 0.01565414109129707), (3661, 0.01564577425342385), (450, 0.015608519656568696), (1361, 0.015592555033603862), (3299, 0.015574789122903308), (85, 0.015565415762667165), (2229, 0.015545140188962478), (896, 0.015539368002936158), (2885, 0.01553066265467311), (4583, 0.0155091381014043), (4669, 0.015492525466058645), (1741, 0.015474293874286435), (481, 0.015469390328392467), (374, 0.015464220140309494), (1512, 0.015450085039927697), (867, 0.015447275691157163), (3642, 0.015425038196230128), (1325, 0.015417810296419088), (1906, 0.015402172315287378), (3694, 0.015394318681617917), (762, 0.015386234332469932), (2376, 0.015381706835274796), (3086, 0.01536640033114927), (4627, 0.015347594022472875), (4134, 0.015345894727775013), (40, 0.015305064222782005), (3306, 0.0152976874344642), (2254, 0.015264388099765314), (358, 0.01524391279622352), (4482, 0.015224543828703422), (3713, 0.015221954853509276), (21, 0.015211614027840471), (296, 0.015204844606541184), (929, 0.015192476876984534), (3407, 0.015189768722261746), (1119, 0.015187159155518683), (287, 0.015182057023698533), (3797, 0.01518071341031898), (4231, 0.015173882829877295), (2522, 0.015160218557647749), (2298, 0.01514742367875594), (2027, 0.0151191157039422), (622, 0.015114877441477752), (1687, 0.015081911122046706), (1115, 0.015076849560100525), (2639, 0.015060665745970907), (1853, 0.015056577491359779), (620, 0.015054170784840127), (2196, 0.015042495092810679), (3580, 0.015039135519098676), (3777, 0.015029275746340404), (4474, 0.014977388808916114), (1880, 0.014966021703830552), (51, 0.014965979411782002), (3253, 0.014939900433374384), (4178, 0.014936139212549819), (429, 0.014907793983901895), (502, 0.014891603243137274), (3437, 0.014891313208532216), (3375, 0.014880736050025874), (1897, 0.01487409258896271), (437, 0.014872318949017253), (3862, 0.014856134944777388), (43, 0.014851289474516489), (1224, 0.014848645936442455), (879, 0.014840329123637929), (543, 0.01481514022208621), (1983, 0.014814705291966625), (4314, 0.01480113606160618), (1290, 0.014782895037111703), (447, 0.01477043861892446), (4379, 0.014738068688333519), (1919, 0.014720185971196648), (584, 0.014718536886619442), (1682, 0.014708572688973999), (2919, 0.014694787924982376), (1278, 0.01469011827176545), (2053, 0.01468579094084932), (2334, 0.014641018727413668), (2931, 0.014636190656546155), (2644, 0.014605903574472971), (1779, 0.014605505493867625), (895, 0.014602672301442823), (3421, 0.014570533357246243), (208, 0.014564317291621241), (2939, 0.014557655967115493), (652, 0.01454961180007468), (2784, 0.01453920272142293), (3699, 0.014528971303086509), (1337, 0.01451632001440457), (1740, 0.014510564426729732), (3558, 0.014470291425645933), (470, 0.014468577429467194), (1895, 0.014460083088388845), (1116, 0.014454249635706785), (4068, 0.014451184354152647), (899, 0.01444837727674443), (1114, 0.014436591435942683), (1192, 0.0143731268998252), (1335, 0.01436626555567386), (3210, 0.01434822359640147), (3670, 0.014346236810449033), (1232, 0.0143343580423758), (1058, 0.014326445616965337), (482, 0.014318865406517198), (957, 0.014312073755375083), (2284, 0.014301377390974099), (510, 0.014297192125796505), (842, 0.014292048885850284), (934, 0.014284810246050515), (2695, 0.014242176019135196), (2815, 0.014233614635509399), (1152, 0.014231082791516454), (986, 0.014213770613722879), (1509, 0.014205028339216105), (370, 0.014201587388961134), (3807, 0.01415004543026814), (2988, 0.014148959205037389), (4486, 0.014142096503967723), (988, 0.014128718827695012), (1483, 0.014114297878227612), (4000, 0.014109337523178098), (1252, 0.014093237016036804), (1331, 0.014069567805799925), (2727, 0.014058481372388208), (181, 0.014055923457905324), (534, 0.01404914416124758), (1621, 0.014022952914941237), (2961, 0.014001569133349953), (406, 0.013996421309263717), (989, 0.013990992406489752), (3356, 0.013971822886881381), (3295, 0.01396915092951471), (2045, 0.013941721469670178), (2216, 0.01394089992970633), (1413, 0.01392252167553847), (2910, 0.013917633478282367), (4255, 0.013906645140043448), (1343, 0.013894810017357654), (252, 0.013883632146620802), (1401, 0.01387271954476124), (4387, 0.013870068941198363), (251, 0.013867966455367267), (799, 0.013866844082999446), (3535, 0.01384066315171278), (1035, 0.01381887453098141), (1967, 0.013818817488233139), (3370, 0.01380740008929319), (1876, 0.013797207843950315), (1461, 0.013796549363393393), (676, 0.013790445822426273), (4673, 0.013777217612414589), (231, 0.013776482994224605), (1481, 0.01376749105730235), (1945, 0.0137474566656582), (87, 0.013731711116033066), (317, 0.01372437577101817), (3660, 0.013717303640745986), (2468, 0.013656866052808383), (18, 0.013639824714195078), (1478, 0.013621453691624496), (2024, 0.01362143661567416), (2366, 0.013612976268805008), (52, 0.013600804094978335), (3861, 0.013592128894296429), (1465, 0.013588900862715182), (775, 0.013580167832495795), (4610, 0.013579403390591703), (3741, 0.013577240544232178), (3312, 0.013575887940800117), (753, 0.013549278832237003), (1591, 0.013536957187268665), (1815, 0.013530410151107168), (905, 0.013521019557386164), (4374, 0.013502565967730251), (2224, 0.013497855033642384), (814, 0.013495540125448381), (3708, 0.013495528700764465), (1986, 0.01349344967712845), (545, 0.013484509510887666), (4124, 0.01345966408865568), (4747, 0.013451885684782254), (878, 0.013435345188327827), (3819, 0.013430728987528886), (2805, 0.013422971549413958), (276, 0.013412243036761688), (760, 0.013408755868769412), (2632, 0.013395941670378386), (496, 0.013381535196328247), (2460, 0.013377406312830293), (1128, 0.01336917289326851), (236, 0.013361417399169878), (2486, 0.013345114807622599), (4524, 0.013344104735653138), (2008, 0.013341066428520627), (4576, 0.013324419282033591), (1665, 0.01331864452408986), (4121, 0.013294058510116134), (332, 0.013291392972049707), (3630, 0.013248693386756738), (1107, 0.013234704742594436), (866, 0.013223819809213744), (1183, 0.013203290150111818), (207, 0.013202287890523336), (2177, 0.013196531145282497), (1864, 0.013194620422679212), (3119, 0.013176467645873434), (3958, 0.013163592055294058), (2066, 0.013148930864670519), (3110, 0.013148818620795283), (4617, 0.013145152122535166), (1667, 0.01310952332403104), (1317, 0.013109511838372383), (4512, 0.013096663788746788), (356, 0.01308537921357196), (906, 0.013082769368796992), (604, 0.013082263186631318), (1802, 0.013074188414515001), (829, 0.013067152965588674), (2121, 0.013060128472127269), (1255, 0.013034577088155506), (1239, 0.013018313167508913), (2969, 0.012999702326476783), (2383, 0.012996311044988591), (1796, 0.012978653060000052), (1360, 0.012946114937554584), (1680, 0.012918757443092243), (1237, 0.01291252967933191), (13, 0.012904730427356216), (4227, 0.012903133125254936), (742, 0.012895262349341564), (75, 0.012892746449532828), (1595, 0.012872864495596305), (7, 0.012848827437220958), (1681, 0.012832438035811508), (875, 0.012828620175361183), (900, 0.01282649488429427), (963, 0.01282335978690511), (3318, 0.012820183098572135), (1342, 0.012818109313890115), (125, 0.012801531158627047), (1000, 0.012794194783292075), (4475, 0.012791476247212132), (1739, 0.012790065058483045), (70, 0.012784303893544423), (3325, 0.012773806745111468), (833, 0.012768979339293338), (678, 0.01274236717803005), (3659, 0.012739067427470985), (537, 0.012728576163409102), (2978, 0.012709399900374011), (1519, 0.012685818153036854), (2874, 0.01266304370471334), (1293, 0.012627559394743807), (2252, 0.012593659017289198), (3076, 0.012578428563124638), (407, 0.012576162839507807), (3768, 0.01255985800340293), (844, 0.012547501024285897), (2617, 0.012541240022816237), (1654, 0.012540361812405912), (3750, 0.012526912155733273), (2000, 0.012490298103748571), (2803, 0.012484307978364386), (2963, 0.012480046815579984), (1376, 0.012474930782576379), (1988, 0.012449725425893047), (1787, 0.01244311834937289), (3637, 0.01243969337920028), (609, 0.012436169884984381), (4337, 0.012416145648083689), (527, 0.012408426657113936), (4510, 0.012406120488644513), (1220, 0.012381759539653547), (653, 0.012376187134664488), (4265, 0.012370029362516657), (1005, 0.01236719175457826), (1436, 0.012367187829493916), (418, 0.012363494963790644), (1567, 0.012359315313796792), (2412, 0.012351300951143736), (3387, 0.012348352343140651), (936, 0.012343388786512692), (800, 0.012330546240660194), (654, 0.012319247296879221), (1185, 0.012314336497917706), (3108, 0.012312576591772555), (733, 0.01230753482660447), (1104, 0.012302637341744903), (667, 0.012288709705708509), (648, 0.012277887423853677), (2052, 0.01225214405332025), (1934, 0.012249159605660146), (1799, 0.012247251568054), (732, 0.01224641375041674), (664, 0.012230253012714354), (635, 0.012208498691708229), (2447, 0.012200094819470354), (928, 0.012197504397565779), (201, 0.012194922563079247), (1047, 0.012178017913835978), (1432, 0.012175283212771795), (1009, 0.012169952798027534), (3849, 0.012140140403992342), (190, 0.012138750265674795), (1949, 0.012117653116043525), (3507, 0.012116777808516594), (2780, 0.012102460227641368), (1542, 0.012101632206248939), (918, 0.012096049309795825), (4095, 0.012071832731641165), (2771, 0.012070015475522526), (1157, 0.012054222172340505), (341, 0.012040276910772649), (2474, 0.012025234810505206), (1714, 0.012011453185764855), (2235, 0.012010628945253024), (4469, 0.012008625600884141), (1812, 0.011945304239266106), (1832, 0.011937535410330451), (1958, 0.011930646176003007), (130, 0.011926867676679177), (1194, 0.011920690598639651), (2788, 0.011899567306988528), (82, 0.011894144332662657), (1407, 0.011883388438677927), (684, 0.01187270882417908), (1310, 0.011857401788079414), (1099, 0.011857342491158735), (3999, 0.011834468356820938), (2005, 0.011813232567949578), (3747, 0.011810499294329865), (452, 0.011805040282430304), (2602, 0.011802879057726746), (4695, 0.011784777485543659), (523, 0.01175475224186366), (149, 0.011746502833415905), (1215, 0.011742448125855624), (1870, 0.011742165690093414), (86, 0.011733847489721559), (4344, 0.011726694019006622), (560, 0.011723796536706639), (1419, 0.011702375166221541), (1396, 0.01169412559915647), (931, 0.011680378019562551), (1455, 0.01167424438890572), (2145, 0.011667846006835805), (3065, 0.011652341121195921), (3317, 0.011650735201311341), (4623, 0.01164624107645406), (2697, 0.011645129052455468), (4148, 0.011642710729146653), (3756, 0.011635471912017534), (2336, 0.011622841866254629), (2913, 0.01160626617783045), (313, 0.011588694147227201), (4596, 0.011579153357762677), (2280, 0.011578581065887973), (1264, 0.011577457331668603), (1090, 0.011525766979697764), (2306, 0.011519597561857308), (809, 0.011480022502538125), (1303, 0.011468723368048096), (244, 0.011434438545935371), (1761, 0.011427305445703435), (1989, 0.011425033991382281), (1406, 0.01142356735170328), (2925, 0.01142089851991689), (1266, 0.01140830004039545), (500, 0.01139692902865105), (2421, 0.011393352490635826), (1249, 0.011389854850356616), (2178, 0.011369102235506752), (825, 0.011336234973378517), (72, 0.011335815706635272), (2057, 0.011335341988602587), (790, 0.011328819098868296), (3957, 0.01130737537328342), (1053, 0.01130468493347921), (4216, 0.01129574202665622), (2688, 0.011271200116927366), (2918, 0.01126091009960449), (3582, 0.011260065662471546), (4543, 0.011258339788766714), (3240, 0.011249340870596558), (915, 0.011247273022572186), (4477, 0.011228675186954683), (1230, 0.011218996224828769), (1873, 0.011193286227882262), (2206, 0.011172300569001004), (4481, 0.011167684757927798), (1262, 0.011152412806465565), (1420, 0.011136701240334801), (2568, 0.011135731584107677), (402, 0.011099556911853728), (1630, 0.011090579239151285), (827, 0.011088505143461765), (2480, 0.011086109421716206), (1012, 0.011077486485627775), (1655, 0.011075509113125723), (3794, 0.011070808538151015), (1019, 0.011046732439510036), (2625, 0.011042436956048845), (1957, 0.01103713744728498), (1054, 0.01103699944625331), (274, 0.011035641459288753), (1852, 0.011027128083942172), (719, 0.011021069857465697), (2555, 0.011014281773315506), (322, 0.011011274215599966), (1551, 0.010990327322037603), (1696, 0.010965269002219375), (1773, 0.010955897824683977), (2346, 0.01092789141982469), (1992, 0.010919745889197363), (4187, 0.010905512014133225), (2759, 0.010896125543937797), (3992, 0.01086432393823145), (417, 0.010857053144102818), (532, 0.010853692109028056), (321, 0.010853546219663456), (273, 0.010851325289581416), (683, 0.010850382331213299), (281, 0.010850110374057989), (3775, 0.010846868308484497), (3118, 0.010846767325738211), (4325, 0.01084142860251558), (538, 0.010837176004175735), (57, 0.010835008478228547), (2429, 0.010834879177906962), (949, 0.01083005059414121), (2062, 0.010827602309256912), (555, 0.010805867563405055), (3993, 0.010799299812975914), (1789, 0.010793270926753161), (304, 0.010776123342338816), (695, 0.010765812704594108), (1858, 0.010754515078436713), (2769, 0.01074689549252221), (4293, 0.01072496987906045), (2680, 0.010718798803295179), (3524, 0.010712545862383618), (4235, 0.010709589001293521), (801, 0.010706865530756116), (1259, 0.010683260447850177), (4164, 0.010674454149190896), (1923, 0.010674188244428695), (291, 0.010654114070260626), (3094, 0.010653611691713995), (4551, 0.010636691906109849), (4032, 0.01062426291591163), (3951, 0.010623974779247279), (148, 0.010606847740924956), (4619, 0.01060441183101697), (3860, 0.010597587690882967), (170, 0.010590419372720969), (1754, 0.010587649198346934), (3924, 0.010565245191918267), (266, 0.010555380119079246), (2739, 0.010547486722511865), (2464, 0.010540963361888974), (1061, 0.010522732972754849), (4048, 0.010521792466705355), (271, 0.010513499130038398), (4366, 0.010509642903648503), (1723, 0.010497387610157081), (501, 0.010495925548300913), (2403, 0.010494032014463658), (468, 0.010463913523735657), (2097, 0.01045894025071592), (847, 0.01044101072550268), (3070, 0.01044100980493831), (3903, 0.010429036686855615), (2992, 0.010426386435022177), (1662, 0.010422019588148998), (3423, 0.010418173494331847), (3426, 0.010402151809410325), (333, 0.010396647172797039), (3099, 0.010396584806118781), (2871, 0.010392979560845669), (1874, 0.010386980241245819), (1694, 0.010377739186490313), (47, 0.010374759033888029), (2051, 0.010344755637093042), (2162, 0.010321303045312511), (2936, 0.010306943195722024), (485, 0.010299890463609936), (737, 0.01026948217402053), (2740, 0.01025165340770671), (354, 0.01023318036745526), (792, 0.010223739969146536), (3822, 0.010223324228813488), (4553, 0.010220370619708468), (3232, 0.010219438024982971), (1339, 0.01021596486720332), (3297, 0.010212639038269283), (206, 0.010195436607244203), (1348, 0.010181205524417283), (1234, 0.010177649958305484), (2436, 0.0101763666679201), (2849, 0.010160919483403277), (483, 0.010147870988533602), (4033, 0.010139571461229513), (2209, 0.010136547687141511), (4605, 0.010113684386539628), (2505, 0.010111741990795405), (99, 0.01010872536394476), (3984, 0.010107881608489588), (1418, 0.010098426231237303), (1658, 0.0100804736714881), (1736, 0.01006161503112795), (270, 0.010051806221174025), (715, 0.010047304304865666), (2049, 0.010037773592981785), (327, 0.010031091446491825), (3382, 0.01002898874098722), (1513, 0.010012053684440077), (4106, 0.010011298899255085), (2546, 0.010005453203518996), (1727, 0.009993058828174554), (2016, 0.009977672051937518), (542, 0.009974966884476081), (2929, 0.00997316401811581), (216, 0.009964319549763758), (1781, 0.00994528192793031), (806, 0.009918568722061226), (120, 0.009912331765059942), (2126, 0.009911946717288973), (2915, 0.009901438303503266), (621, 0.0098894425959586), (979, 0.009887972165231157), (1300, 0.009883442651908877), (2074, 0.00987182120936709), (3674, 0.009866519236776755), (1334, 0.009866451708928596), (2116, 0.009826879593775987), (2494, 0.009816473373279778), (0, 0.009805093506053453), (2489, 0.009794792049552446), (1359, 0.009783798724744835), (3142, 0.009781933944899053), (2820, 0.009780711952702378), (1708, 0.00977923271618291), (1798, 0.009774556470432893), (994, 0.009767338355605823), (4371, 0.009763787259413185), (1440, 0.009759613744201243), (544, 0.009753397860988314), (1092, 0.009742359298906326), (1712, 0.009732335194850533), (2964, 0.00972958693050268), (3949, 0.009725553805078438), (3218, 0.00970686767527964), (1619, 0.009703084106321473), (1922, 0.009702305857966465), (3679, 0.009695639399177612), (2934, 0.009681263395234521), (3155, 0.009676985323238005), (3635, 0.009666279084388135), (1951, 0.009660200117561584), (2565, 0.00965865847843089), (243, 0.009658171853199466), (4435, 0.009657090753751577), (2418, 0.009651250070554153), (5, 0.009639835665946627), (1685, 0.009633240613946496), (4052, 0.009622904531408717), (3612, 0.009614913459816828), (3264, 0.009614029034340891), (4158, 0.009601381761401219), (1075, 0.009591487522932454), (2250, 0.009590492035507887), (1442, 0.0095890271815945), (2633, 0.009558772985519754), (4060, 0.009548933425246275), (2512, 0.009542271470272569), (105, 0.009532098755129267), (2640, 0.009526668488920899), (894, 0.009520951455559387), (1438, 0.009518400966834185), (3919, 0.009518026688365582), (1006, 0.00951241049788545), (3888, 0.009509824437820174), (3599, 0.009506751045859305), (288, 0.009496377944736414), (2601, 0.009495593230104763), (1475, 0.009491808199921726), (2545, 0.00948600870856867), (435, 0.009477836158719864), (2655, 0.009474781634864609), (1048, 0.009461601719983486), (2197, 0.009457720469104737), (1338, 0.009453093408532395), (970, 0.009447726677397602), (3536, 0.009447284878491278), (4025, 0.009445947734436947), (1124, 0.009439593845048234), (2744, 0.009436372522052039), (3689, 0.00941773693384183), (1279, 0.009414733311017304), (78, 0.009399606571884909), (1382, 0.009398048957401735), (2029, 0.009383399674635615), (1494, 0.009379897367766055), (472, 0.00937363469527576), (2075, 0.009368083693250751), (4444, 0.009365545280548903), (2279, 0.009364676134641814), (1860, 0.00936372403435563), (631, 0.009361669401453363), (3215, 0.009351852172126342), (2977, 0.009322674076250256), (4442, 0.009322506640795744), (4192, 0.00930711991890133), (1936, 0.009305710762007566), (1077, 0.00930179774986171), (2789, 0.009294840803167722), (1182, 0.009289577849239705), (2080, 0.009286183430238319), (1688, 0.00928447679177188), (850, 0.009269227266584062), (1087, 0.009256627090253322), (3643, 0.009249751025514882), (353, 0.009247286364833024), (668, 0.009247180014652573), (2798, 0.00924585532579227), (4546, 0.009241565345370469), (396, 0.009236073372609652), (2277, 0.009229634965057291), (1582, 0.009227189264785263), (3386, 0.009225598651981193), (2255, 0.009224149251331642), (2948, 0.009213541283917926), (2752, 0.009192679728709074), (2193, 0.009187834696774063), (2144, 0.009184136725802351), (182, 0.009177613098031678), (1854, 0.009176487834003655), (897, 0.009174254862381888), (2886, 0.009169658422198456), (104, 0.00916249023695782), (2228, 0.009156965667265397), (697, 0.009143071449328686), (3171, 0.009142617878024973), (1160, 0.00912265594299187), (2831, 0.00911547050081377), (3293, 0.009096992545310073), (434, 0.00909271578475179), (3346, 0.009080805971871126), (828, 0.009079231893502364), (79, 0.009076618790839581), (1612, 0.009066688687457697), (939, 0.00906544737876302), (4511, 0.009055944146683143), (346, 0.00904732990567095), (4710, 0.00903722525774957), (3596, 0.009010933192656957), (3941, 0.009006728347892528), (1948, 0.00900217093487605), (464, 0.008999856286562488), (3067, 0.008994762392335234), (3237, 0.008993087333431068), (1620, 0.008987057234226398), (2463, 0.00894983822573773), (4685, 0.008939084683528015), (119, 0.008932839836200659), (1807, 0.008930900977394138), (3046, 0.008930165950430557), (2980, 0.00892969508928226), (111, 0.00892830755196627), (2600, 0.008926105435859566), (3638, 0.008913892551018446), (948, 0.008908360175058827), (2087, 0.00890534030263058), (4612, 0.008900541314353928), (3667, 0.008900171105382566), (3120, 0.008898319654514026), (96, 0.008895438584707134), (1900, 0.008883222611181612), (446, 0.00888200665157438), (2698, 0.008871041588029817), (2103, 0.008865792807943298), (558, 0.008862695499612721), (1096, 0.008857925187504443), (2581, 0.008841135380210335), (1701, 0.008829989975010642), (4660, 0.008816293072121558), (817, 0.008811076124523943), (3521, 0.008807933706918614), (4336, 0.008794656199100885), (651, 0.008790443518269624), (4122, 0.008786711827347365), (19, 0.008784739948684396), (4502, 0.008778213671318655), (3826, 0.00875332692435902), (2363, 0.008743311125802651), (782, 0.008737001055913084), (1020, 0.008735245570264399), (3246, 0.008728646467293667), (2188, 0.00872547504917266), (1446, 0.008725319988941804), (3418, 0.008722324977241057), (3267, 0.00872099401762529), (3123, 0.008720722046885655), (1276, 0.008718177494154983), (2879, 0.008707067714400177), (2143, 0.00870524190616186), (285, 0.008704678727235576), (2459, 0.0087021962221496), (2309, 0.00869760131422764), (1387, 0.008676472959391519), (3151, 0.008673167385631366), (3733, 0.008671664222620296), (2473, 0.008671326295738156), (3784, 0.008666453071715974), (164, 0.0086637829941784), (2778, 0.00864507950538454), (2065, 0.008634933847474484), (962, 0.008633517179123244), (2077, 0.008628455950862961), (2572, 0.008624926760274992), (1710, 0.00862480157860797), (3901, 0.008622386333348418), (197, 0.00859704253241558), (966, 0.008596738901221878), (1429, 0.008595043377298776), (3954, 0.008593121833034324), (2303, 0.008587247057459328), (2812, 0.00858075314838778), (4257, 0.008577179765386033), (3956, 0.00856647521911965), (307, 0.008540452172185265), (2264, 0.00853872494735178), (1793, 0.008533810434469269), (734, 0.008527107655238415), (4664, 0.008516099300011862), (1206, 0.008511491354820998), (3399, 0.008506480833147213), (4603, 0.008493147032227942), (368, 0.00849246998822155), (4490, 0.00847884672726767), (921, 0.008473884306744563), (838, 0.00846638251021233), (1776, 0.008464441636809431), (3829, 0.008463648801411847), (1650, 0.008442906417332422), (1514, 0.008426393019628341), (851, 0.008419793419722108), (1920, 0.008418614385203606), (2089, 0.00840106321112749), (1477, 0.008398088250305705), (1968, 0.008396226262273387), (461, 0.008378393185575846), (4412, 0.008375126016394905), (3389, 0.008373948421723199), (4649, 0.00836168035627167), (1875, 0.008361119199879558), (4232, 0.008355629863574444), (1308, 0.008353487600809638), (183, 0.008350342502147893), (3329, 0.008323855378347707), (2427, 0.008304726949703233), (1730, 0.008300929366563799), (2635, 0.008290017471095085), (4163, 0.00828909244186234), (443, 0.00826944426866319), (2265, 0.008265713268684284), (1540, 0.008264873545767479), (1538, 0.00826452714849783), (2236, 0.008262153855153739), (2158, 0.008249182115915604), (449, 0.00823467413153059), (1690, 0.008203297599856187), (2285, 0.008192880614420481), (1050, 0.008188052484759224), (597, 0.008184692697223068), (1924, 0.008167974470972303), (1971, 0.008146467998911179), (4205, 0.00813259415956046), (1762, 0.008122600557858468), (1539, 0.008118828372420506), (107, 0.00810878589263473), (2076, 0.008106110318529727), (3960, 0.008105392582227868), (1507, 0.008102011472032189), (2881, 0.008097352464452926), (4092, 0.008090895367233297), (38, 0.008085428274959462), (3680, 0.008084768946688057), (2587, 0.00808003809866371), (4494, 0.008076927428852684), (4699, 0.008066732917858166), (705, 0.008060671056134337), (4335, 0.008058701805706186), (1553, 0.008035712147274676), (1489, 0.008033719451971282), (3196, 0.008017179405249625), (3, 0.00800429043895183), (1078, 0.008004074147420881), (3032, 0.008002698145813185), (436, 0.007999143568905942), (2975, 0.00799910472417184), (32, 0.007984548069367697), (1136, 0.007982223371637606), (2840, 0.007974038146102615), (729, 0.007972578233613352), (4593, 0.00795009926001135), (1498, 0.007948536519158821), (4105, 0.00794159514227583), (2854, 0.007940287278032943), (139, 0.00793805341964405), (924, 0.007930889582430515), (4707, 0.007924309197114073), (688, 0.007920082561582203), (1960, 0.00791594458958931), (3096, 0.00791471142124377), (2304, 0.007905045081506133), (1764, 0.007892329915581534), (1260, 0.007892175187202838), (2428, 0.007890164359013144), (4748, 0.007885550521461237), (242, 0.007883152373824122), (2942, 0.00787876782175488), (1371, 0.007859168909794434), (1454, 0.00785287184664528), (4046, 0.007837863472015384), (385, 0.007832134714130213), (1790, 0.007830652807786428), (4601, 0.007825524342012363), (816, 0.007822688625960025), (3192, 0.007816038194544937), (1866, 0.007806781469902531), (1833, 0.0077965095169583885), (4133, 0.0077958126868276235), (445, 0.007794521839692808), (4522, 0.00779142357392963), (60, 0.007788672977779784), (4013, 0.007783966541683047), (350, 0.007783455522120415), (3453, 0.007781907770548946), (3516, 0.007775657982650567), (3579, 0.007771852322868443), (162, 0.007770799696963449), (1743, 0.007750090589066046), (3771, 0.007743879506289292), (582, 0.007738614071243571), (2933, 0.007732280496939367), (3704, 0.007726207293318316), (2477, 0.007724564644052247), (1806, 0.007724060987961749), (1674, 0.007717885024911842), (403, 0.007717320665807713), (728, 0.007711282099805773), (4579, 0.007706345424758964), (3899, 0.007704160140244185), (3634, 0.007698238156314156), (3112, 0.007688011853815088), (1312, 0.007683696684100865), (991, 0.007674540016661659), (3256, 0.0076572783933819), (1140, 0.007655221232160154), (1537, 0.0076545522894884395), (2603, 0.007647101042214018), (4431, 0.007646034470317188), (4038, 0.007643493182656478), (2949, 0.007639155147339895), (3456, 0.007637110780276211), (3821, 0.007635870656724133), (2104, 0.0076355178680262425), (3780, 0.007633761812979329), (1071, 0.0076296938801074105), (4118, 0.007629579528410197), (4656, 0.007629219763180771), (2211, 0.007629219619822573), (3586, 0.007614155228395089), (1014, 0.007610412264289004), (493, 0.007590992590773915), (930, 0.007588642360831522), (616, 0.007587604885805269), (4094, 0.007582355866076667), (3618, 0.007578451625313122), (1705, 0.007576217404227394), (2714, 0.007566646462252822), (1282, 0.0075637968823544744), (1484, 0.007562813857263789), (180, 0.007560424083753987), (1918, 0.007551945563332286), (1225, 0.007542388898273974), (10, 0.007539724639541887), (1400, 0.007536440370065782), (4289, 0.007530304372005355), (2563, 0.007530270288055348), (2510, 0.007529972715630197), (1571, 0.007527686704103847), (441, 0.007524058999258837), (2844, 0.007519917586582681), (1902, 0.007514941436228623), (4757, 0.00750809522210286), (1643, 0.00750602651388331), (4557, 0.0075049104273801175), (1188, 0.007504203984202115), (3464, 0.00749830788075648), (716, 0.00749730430513755), (4624, 0.007497150714487852), (4233, 0.007493601501957861), (2088, 0.007490653097136644), (843, 0.007487678947366412), (113, 0.007487310843562389), (255, 0.007486787644460759), (4430, 0.007485544625895459), (845, 0.0074849403670845475), (3905, 0.0074838650684981665), (4045, 0.007474521320913149), (580, 0.007471013806577874), (660, 0.007468299121380835), (1229, 0.007464115927586654), (3514, 0.007463910276476754), (3259, 0.007461484276829566), (2873, 0.007460728637960147), (2339, 0.0074607042887312154), (4629, 0.007458366306468024), (4089, 0.007444294164478699), (34, 0.007439622267479848), (1083, 0.007438831750066306), (1950, 0.007437122534097678), (474, 0.007434113526945559), (3039, 0.007433241299459784), (3666, 0.007423488483315582), (143, 0.0074218727251426225), (3349, 0.007417544683405595), (1037, 0.007406593398245866), (156, 0.007396517906534802), (980, 0.0073892674550401615), (3018, 0.007388671328103669), (3945, 0.007385100505287984), (606, 0.00738281553042624), (4249, 0.007376866463428255), (3623, 0.007375385289240741), (4470, 0.007371133673986452), (1536, 0.007357200882370105), (3233, 0.007355187520740297), (224, 0.007353548211987467), (4390, 0.00735207097581671), (1069, 0.007349470531851638), (743, 0.007346838592574463), (3008, 0.007343589760949153), (509, 0.00733202705436811), (4098, 0.007328628147016927), (3410, 0.007326878072907434), (3571, 0.007310855744198967), (1174, 0.0073090099747231945), (1931, 0.007304840964451408), (2519, 0.007297888997678442), (1735, 0.007296268013052199), (2843, 0.007294454990914622), (238, 0.007292058096564207), (3653, 0.007288033329822759), (750, 0.007283807541207738), (3303, 0.0072756740838892334), (3501, 0.007267483112732892), (1144, 0.007259122310498271), (869, 0.007254016902358079), (2091, 0.00724908335407164), (63, 0.00724637379048299), (3645, 0.00724440879850767), (309, 0.007241873038964715), (2061, 0.007241444441148378), (4077, 0.007237935229267639), (4093, 0.0072372475745065045), (42, 0.007236825272071698), (1486, 0.007234166049300601), (1472, 0.007232693801577943), (1138, 0.007232291199342742), (908, 0.007227807872197648), (4677, 0.007226291498591362), (2244, 0.007224478463281346), (636, 0.007220498423054623), (2444, 0.007216822945365926), (3227, 0.00720882098845807), (2606, 0.007198949096365795), (1583, 0.007196604196620224), (696, 0.007196443040031081), (3436, 0.00719553939447874), (4517, 0.007192818112932041), (2101, 0.007188361400101866), (3125, 0.0071848861424403995), (4226, 0.0071813010126941775), (256, 0.007180422705514563), (363, 0.007177918653319793), (1191, 0.007177768471697236), (1223, 0.00717722505421251), (4061, 0.007175096904403546), (4715, 0.007168016491301172), (1488, 0.007167547433373899), (2344, 0.007164432520815709), (4196, 0.007152503548435217), (1179, 0.007148580085663995), (3245, 0.007148416664097887), (3515, 0.007141768857087135), (4581, 0.007140956745791369), (159, 0.007126037020866246), (2994, 0.0071209261581707105), (494, 0.007107534761405225), (1388, 0.007105864043348033), (3152, 0.007105099502527769), (4184, 0.007103928823641512), (1811, 0.007092076580957013), (3727, 0.007088736271485593), (1747, 0.007085757718312184), (3624, 0.00708332047076107), (3435, 0.007080080814085195), (232, 0.007072494943779912), (340, 0.0070577890082476336), (769, 0.0070559764342692744), (880, 0.007046905349603812), (4351, 0.007044390945365722), (3195, 0.007035857525779765), (3570, 0.007030792303727618), (2069, 0.007024574301463462), (727, 0.007024317991323226), (3499, 0.007023650271851442), (4284, 0.007015060521553908), (413, 0.007014363525749394), (81, 0.007009943535800456), (1504, 0.007007295859807677), (1737, 0.007007001454081945), (3316, 0.007003850870270371), (3457, 0.007003019585887427), (3185, 0.007000170786572425), (2825, 0.00698930913622386), (50, 0.006986992676753986), (4299, 0.006979491877667861), (4309, 0.00697819374420941), (1653, 0.0069720422336954115), (748, 0.0069703375048933616), (4652, 0.006959441062191511), (301, 0.0069485776645648555), (1330, 0.006945237124300198), (1044, 0.006925941771792754), (539, 0.006923300446519886), (600, 0.006911988221385433), (4182, 0.006907818896450108), (217, 0.006895954353204596), (3696, 0.006894880242524032), (1421, 0.006892431195663454), (1718, 0.006885352976791461), (923, 0.0068851967951298505), (503, 0.006882371442124131), (3487, 0.0068740778119156035), (752, 0.006874003656088703), (3531, 0.006862294924219214), (4670, 0.006848594424887118), (386, 0.006839997396687533), (4523, 0.006839334010413386), (2691, 0.006834099053790853), (1841, 0.006832081872064486), (3149, 0.0068243582803357815), (1911, 0.0068215375429680905), (3122, 0.0068204751632027355), (1076, 0.006819943767270469), (4008, 0.006817202182472819), (1001, 0.0068140912017435416), (3035, 0.00680633588123159), (1125, 0.0067987645178981225), (2816, 0.006796760437225053), (3648, 0.0067966355837907584), (1375, 0.006795276578803917), (1123, 0.006794885124020777), (644, 0.006791787033115819), (4467, 0.006785277754309836), (671, 0.0067828701196653), (2726, 0.006782846187248172), (1231, 0.006779688354393065), (367, 0.006777740856868494), (3265, 0.006769470229076111), (778, 0.006760120126778052), (2897, 0.0067578748204000574), (4388, 0.006755130022591245), (3734, 0.006743290499240995), (1177, 0.0067349171277387735), (2348, 0.00673431186581514), (2962, 0.006732649301460031), (31, 0.006723965537835127), (2899, 0.006720886243817159), (1738, 0.006716538657576399), (3632, 0.006714251426310356), (1111, 0.0067125880140789735), (1041, 0.006711122649795384), (2732, 0.006699254917744875), (2708, 0.006695604248962895), (1250, 0.006695136066226618), (56, 0.006687995450791239), (2496, 0.006686100058633569), (422, 0.006684770214378324), (1425, 0.006682409645770868), (3452, 0.006666829518739313), (283, 0.006663066484764481), (4210, 0.00666279625006107), (1819, 0.006660823685789856), (1555, 0.006655728045330869), (131, 0.006655142039509908), (1433, 0.006651536462062502), (4591, 0.006649489713339693), (2184, 0.0066460697561804795), (311, 0.006640720103355573), (3342, 0.006638970720780707), (868, 0.0066380990252306385), (1306, 0.0066374175223380336), (2335, 0.006626868445508635), (758, 0.006619783688263925), (744, 0.0066118215152692235), (1760, 0.006610240515573115), (1448, 0.006606255011892964), (1908, 0.0066037384583795015), (4282, 0.006581235977916588), (4001, 0.0065798866522937954), (3926, 0.006579383573264013), (1172, 0.006576811496944065), (3460, 0.006574404057633163), (1374, 0.0065735766582562015), (4099, 0.006567093402415353), (4738, 0.0065658473500210725), (3033, 0.006565105720620909), (3876, 0.006562838398218208), (1644, 0.006561402643121727), (1501, 0.006560512948820128), (1462, 0.006557735573350133), (1345, 0.006554266558119459), (910, 0.006544699287657487), (2324, 0.006544521660283181), (3594, 0.006542877340613763), (745, 0.006541447895988961), (863, 0.0065353030348067245), (1065, 0.0065346759690377235), (1238, 0.006524049508288304), (22, 0.006522322352622825), (122, 0.006517403480064114), (834, 0.006515346842433373), (2503, 0.006513803988319437), (996, 0.00650992907297042), (1692, 0.006499365798951296), (3474, 0.00649658195092293), (1987, 0.006494419384748071), (1892, 0.006492138216479109), (1867, 0.006487323100488623), (1913, 0.0064824046591955295), (1329, 0.0064822128175896394), (608, 0.006480886036499979), (3705, 0.006469532567629695), (1849, 0.006466697460137597), (1964, 0.006462905219506746), (4154, 0.006460444818820417), (2031, 0.006451642626205173), (563, 0.006446918984242734), (581, 0.0064429088076600515), (3842, 0.006439580046008823), (981, 0.006436594763438926), (804, 0.006430481765266979), (1094, 0.006428490781993139), (3288, 0.006427108303657308), (3066, 0.006417860970259336), (2424, 0.006412851568886809), (3841, 0.006411621947297271), (2239, 0.006407566328685134), (230, 0.00639704758425901), (2580, 0.0063848130308622525), (1414, 0.006378299226169405), (1816, 0.006377671673092274), (940, 0.006372201502734289), (4367, 0.00636561455566984), (2724, 0.00635309231256632), (1267, 0.006350083320400627), (4217, 0.006344514387184781), (2095, 0.00634399459508417), (4661, 0.006337486653117293), (2056, 0.006329973382063176), (3998, 0.0063284474489425134), (4564, 0.006324868664687002), (521, 0.006324471633262136), (4459, 0.006319462824825345), (200, 0.006317406038489515), (1608, 0.00631080660484277), (4303, 0.006307820224547157), (2833, 0.006306426535276037), (497, 0.00629601813997159), (1552, 0.0062804575791378355), (1526, 0.006277220093134095), (3910, 0.006276866044991001), (3309, 0.006272591746028671), (300, 0.006258139455269685), (4432, 0.006257829146207155), (4691, 0.006248887308908626), (1327, 0.006246469827302094), (4666, 0.00624575032328202), (3458, 0.006237886369444205), (2388, 0.006227393088748629), (1818, 0.006224779631552357), (1664, 0.006221292918029591), (263, 0.006216251561942655), (1213, 0.006215002337363142), (835, 0.006210819751878022), (1797, 0.006202669692847393), (3864, 0.006198950838403933), (2202, 0.006188384803965121), (1307, 0.006181668255159588), (2160, 0.006181185621205105), (642, 0.00617554124475728), (3566, 0.006170320282172521), (862, 0.006163646870521245), (861, 0.006156676188760678), (2205, 0.006148708939289658), (1903, 0.006144808322546005), (1746, 0.006130600381762394), (3909, 0.006128669375239794), (1939, 0.006122496770723247), (3721, 0.006120051103397477), (1627, 0.006111510124918706), (568, 0.0060923938011236784), (9, 0.00607882290416431), (248, 0.006076898456420151), (4236, 0.00607498699543385), (3114, 0.006072588491821387), (4009, 0.0060694965649699005), (2175, 0.006065790209232859), (35, 0.0060612328203774185), (4342, 0.006053130571462052), (1356, 0.00605131280670182), (617, 0.006036313815003582), (3244, 0.006017414560259967), (821, 0.0060159760666970525), (3975, 0.006013273983329386), (2203, 0.006010749392625514), (4537, 0.006005299509575737), (958, 0.006004028909589244), (4733, 0.005965512302462513), (2355, 0.005960565575827434), (3331, 0.005959816487740433), (16, 0.005959078936688496), (583, 0.005955003048448513), (3715, 0.0059530536022729275), (3658, 0.005945222312437101), (1214, 0.005932567568348967), (3825, 0.005930841255515678), (4219, 0.0059307558518514976), (2058, 0.005927826803031612), (4055, 0.005924818293621736), (2426, 0.005920751565415964), (1316, 0.005910781285140436), (1981, 0.005908455371472134), (2185, 0.00588469360959802), (1715, 0.005883156475360245), (4646, 0.005882073074407983), (4464, 0.005865917370922849), (3865, 0.005858147278425384), (2156, 0.005849206467237161), (4057, 0.005838723038181404), (2935, 0.005833966818310372), (4047, 0.0058310531983781005), (4110, 0.005829926434041166), (3598, 0.0058148858738907615), (3844, 0.005781129296899576), (4208, 0.005772631262084199), (953, 0.005756518916356405), (1684, 0.005754002436817411), (4674, 0.005742313437079809), (3049, 0.00572814392853459), (1344, 0.005721039864961347), (4385, 0.005717363384544328), (3509, 0.005699119019090606), (3748, 0.005683490190282457), (1863, 0.005673121301952915), (3588, 0.005668212447753092), (2328, 0.005662324030417309), (3391, 0.005654239730508646), (4653, 0.005640484385845355), (2291, 0.005627749684426434), (3942, 0.005627567292449441), (2098, 0.005618888882314847), (3744, 0.005614568383030678), (4518, 0.0056003864349854155), (177, 0.005599808753936733), (3448, 0.00559647446856459), (3502, 0.0055839873596376976), (3752, 0.00558054137277933), (4514, 0.00558021931038109), (4698, 0.005566055076203875), (3164, 0.0055627503744931995), (1941, 0.005521670047666052), (571, 0.00551243089187356), (512, 0.005483270579141841), (2567, 0.005474566349004076), (2273, 0.005445167150185859), (4642, 0.005444385938077968), (562, 0.005424022281125922), (3940, 0.00541580878603716), (369, 0.0054147171174585024), (4285, 0.00541390337248493), (2665, 0.005408896703823956), (2439, 0.005393098007991499), (1940, 0.005391940370749308), (3022, 0.005367062238452818), (3440, 0.005360191089565495), (4726, 0.005357462984646266), (2809, 0.005339089482851617), (1695, 0.005316808464005938), (4331, 0.005314131386390756), (4162, 0.005309960252153657), (4527, 0.005304592026024582), (380, 0.0052998836952428295), (1381, 0.0052941344423078724), (3117, 0.005288750302616192), (1453, 0.005285281631882958), (855, 0.005267649046133167), (4261, 0.005249130933861092), (2774, 0.005249022144044434), (477, 0.005239784974437232), (2181, 0.005236538353974075), (425, 0.005233653978455374), (4746, 0.00523258618884702), (2576, 0.0052191298618978746), (4462, 0.005213474094856588), (2022, 0.005209538508579561), (3168, 0.0051948318476039), (666, 0.005191363840721598), (2700, 0.005182671029789315), (4307, 0.005179565875975142), (4630, 0.005173595112168345), (3158, 0.005170714049097465), (2683, 0.0051675037568785385), (168, 0.005162629015437511), (1158, 0.005154276117296022), (1391, 0.005146892045916608), (4120, 0.005142394346497135), (4043, 0.005142156064116709), (2113, 0.005140329245801168), (1332, 0.005140102469137354), (1962, 0.005139410447659317), (4515, 0.005133628241484277), (3180, 0.005132573372863185), (4119, 0.005127533389383312), (2733, 0.005124706672572313), (687, 0.00511838964431733), (128, 0.005117957196142506), (2231, 0.00509809890783702), (550, 0.005095713449789213), (1554, 0.005079354545010316), (2314, 0.005075043982713094), (595, 0.005073766918951453), (4091, 0.005069099168848594), (3604, 0.005067139324779593), (69, 0.00506551508596364), (2626, 0.00506321164286469), (1167, 0.005054247756466491), (3802, 0.005051573170028611), (3787, 0.005050684028750155), (802, 0.00504790855259478), (831, 0.00504729347668347), (102, 0.0050401893607578485), (4240, 0.005036241334993982), (3263, 0.005025888185502877), (1829, 0.005021692709172187), (3163, 0.005021375235815922), (513, 0.005015028264463551), (303, 0.0050061679094136795), (514, 0.005003024616850094), (3938, 0.005002076654805726), (2136, 0.004999931651805338), (4595, 0.004991963728483643), (2599, 0.004986212320267052), (2084, 0.00497883099639507), (1150, 0.004975946962821241), (3468, 0.004972065267270442), (4090, 0.00497122442224054), (4076, 0.004970043121679035), (1661, 0.004967986400080027), (1952, 0.004967831528029215), (1724, 0.004967362630089575), (6, 0.0049636657561850026), (420, 0.004960790573790974), (4312, 0.004956559811046084), (3584, 0.00495460907849746), (4373, 0.004944937742506397), (3451, 0.0049447961135720125), (3782, 0.004941626446775452), (3774, 0.0049401024395021535), (1575, 0.00493962475567439), (3131, 0.004935719359181448), (992, 0.004935502243441057), (1614, 0.004935318091384703), (414, 0.00493284652771533), (1732, 0.004930749603787047), (3438, 0.004925075352046846), (1659, 0.004917338400093204), (2283, 0.004916374937626596), (1280, 0.004912549776270106), (4719, 0.004912020457018882), (1791, 0.004911393510206823), (3997, 0.00491138185917065), (3710, 0.004904565905805378), (2044, 0.004900368156440432), (239, 0.004893411026998544), (3897, 0.004891332365552052), (2208, 0.0048896326651322545), (1426, 0.004887726304196335), (2819, 0.004887152493105063), (4384, 0.0048863605224429355), (3205, 0.004886156117287779), (1904, 0.004878866675051578), (2330, 0.004877726866423949), (220, 0.004877383327231498), (1452, 0.004876297175437618), (765, 0.004875714723265432), (1531, 0.00487448226189164), (1502, 0.004871803904837503), (1380, 0.004865433624290717), (1859, 0.004864612361744439), (891, 0.004859604317280072), (1975, 0.004859271928670793), (4392, 0.0048578911171751425), (1449, 0.004856782191775572), (2959, 0.004856626562989746), (2790, 0.004850603519905103), (561, 0.004843879649288874), (2064, 0.0048383411344764616), (320, 0.004836468342738552), (3513, 0.004833569400596494), (4639, 0.004827393660535323), (1881, 0.004825322882698362), (3769, 0.004823654473202804), (4621, 0.004820847396153738), (1588, 0.004820371979478831), (2015, 0.004817274786074442), (3134, 0.004815055879995134), (4586, 0.0048038743900341956), (27, 0.0047922703978129), (793, 0.0047911708785747225), (3124, 0.0047897235355676224), (3907, 0.004786368378027254), (4275, 0.004783375335158279), (3995, 0.004783012688872665), (4552, 0.004781914462610898), (189, 0.004777355844485406), (1469, 0.004775977068505571), (3398, 0.00475799272399742), (3191, 0.004749484075312184), (95, 0.004745609331166691), (685, 0.004739140064506008), (3179, 0.004737186136549798), (4377, 0.00473449738414215), (118, 0.0047336369622742935), (902, 0.004732429780589892), (4376, 0.00472987449563689), (4251, 0.004729825034580443), (2947, 0.004728489945670273), (1901, 0.004728085067675583), (1431, 0.004724038283531271), (1435, 0.004716569576995678), (4678, 0.004715176978610753), (336, 0.0047110789913987), (2960, 0.004705331125110952), (3815, 0.004703487539245398), (1587, 0.004696037086649698), (3404, 0.00469377408637166), (919, 0.004688274887806511), (3576, 0.0046855570241939055), (3833, 0.004685092741441777), (2278, 0.004680281026963687), (3932, 0.004678398488262888), (811, 0.004677175365825214), (2991, 0.0046748260207572076), (3908, 0.004674093092431092), (3520, 0.00467025158615055), (1998, 0.004669056138259162), (1930, 0.0046636733428292625), (2130, 0.004663428752584404), (3005, 0.004662843276282043), (30, 0.004648836119227042), (4103, 0.004638354930990023), (4360, 0.004638002055274865), (451, 0.004633317948990186), (39, 0.0046323263203813065), (4383, 0.00462950343379809), (347, 0.004629011445466316), (2506, 0.004628370144810393), (315, 0.0046275791609617966), (3367, 0.004620646774560632), (4310, 0.004618064119380746), (1566, 0.004617094549750663), (849, 0.0046103472537448245), (135, 0.004609422560900165), (305, 0.004608912986979318), (2246, 0.004604721551112668), (389, 0.0045928926555422215), (619, 0.004592008813534647), (460, 0.004591946474043866), (4248, 0.004586070327996085), (3432, 0.00457959570783518), (4708, 0.004578152801117167), (4665, 0.004575605255719265), (375, 0.004559317565774011), (2847, 0.004554869102789387), (233, 0.004553254985288596), (3161, 0.004551187168761801), (3443, 0.004550394474658327), (467, 0.0045476787092075905), (4264, 0.00454624722656051), (1573, 0.004544910721244759), (1857, 0.004541703501595063), (1127, 0.004540712375358485), (3602, 0.004536165102704674), (1622, 0.004534966118457996), (634, 0.004532017668175815), (1082, 0.004530923132656162), (4211, 0.004528622817440264), (927, 0.004525247754470468), (1635, 0.0045244140400680045), (633, 0.0045195689450570255), (90, 0.004511298820312949), (2232, 0.0045071342704136605), (4039, 0.004497181173511471), (1933, 0.004496946860875293), (1846, 0.004494151496336112), (1953, 0.004482532871190866), (152, 0.004480162377431886), (3583, 0.004479553777020868), (3555, 0.004471280542747129), (1347, 0.004456071224498093), (2245, 0.0044559238644446015), (3011, 0.004454894047740582), (2432, 0.004446831956179276), (3664, 0.004434450523125298), (310, 0.0044324607065052745), (3886, 0.0044305555437740545), (1632, 0.004423258499538447), (4438, 0.004422951263287813), (93, 0.004418656840322172), (3126, 0.004418094007533676), (3970, 0.00441235901817224), (1633, 0.004408178160738385), (1207, 0.004407380155076317), (1993, 0.004404753943201429), (3824, 0.004403203520833348), (3881, 0.004399498239922743), (4587, 0.004396915493480532), (2711, 0.004389725240886559), (2787, 0.004386794249015826), (4441, 0.004382409607814833), (1631, 0.004376975220158413), (260, 0.004375759434559263), (1428, 0.0043732088719860346), (1211, 0.004371438026142519), (3361, 0.004367134773433362), (4071, 0.004365080839408345), (4151, 0.004357507674573638), (3723, 0.004353829586358225), (4292, 0.004346641270334503), (3823, 0.004337632521968427), (3133, 0.004336292620515619), (1914, 0.0043357717271408636), (1451, 0.004333419161392226), (2139, 0.004329829930682734), (661, 0.004327776691481764), (3135, 0.004320968927313894), (974, 0.00431872120142841), (4585, 0.004316825219797294), (426, 0.004315083525299143), (3788, 0.004312418804018253), (810, 0.00431024470610246), (4328, 0.004309779076309047), (3100, 0.0043093976297925605), (2682, 0.00430424398851454), (3136, 0.004302789301984928), (3966, 0.004302620439293622), (3338, 0.004298076523995532), (690, 0.004292327916105059), (2442, 0.004290553298955562), (2660, 0.004289301064415874), (4697, 0.004288320125964997), (1480, 0.004288052651907407), (3143, 0.004284662611376249), (316, 0.004275668536878031), (1562, 0.0042731699418304), (1623, 0.0042720073056617385), (3079, 0.004251719719739137), (306, 0.004250577618359522), (1197, 0.004241742454974192), (94, 0.004236585948952706), (2984, 0.004235521067904496), (4274, 0.004230225814165784), (80, 0.004227109798982706), (4322, 0.004224059410919858), (397, 0.004218130295350773), (4339, 0.004214172565029606), (1281, 0.004210757877745523), (1840, 0.004197512097260954), (4193, 0.004195492760646212), (1784, 0.004189175005907085), (3534, 0.004188386236756716), (4044, 0.004185917988001526), (3247, 0.004172448145238135), (4290, 0.004163826251867192), (893, 0.004160011744378803), (898, 0.004155926036290059), (997, 0.004149127110904068), (2678, 0.004130445306673907), (323, 0.004126702166598835), (932, 0.0041240318599223), (803, 0.004123319018849689), (191, 0.00411617790201361), (4582, 0.004115089528140448), (1154, 0.004112052748094562), (559, 0.004110087166529763), (3495, 0.004102292524056775), (611, 0.00407474121950208), (4365, 0.004063496237183203), (2299, 0.004055627755214389), (3160, 0.004052363978554839), (756, 0.0040510836090402675), (3619, 0.004047587780381726), (187, 0.004046624716605281), (4571, 0.00403004995905347), (4468, 0.004028035082793067), (1925, 0.00402731300929992), (1590, 0.004022298707395246), (3178, 0.004009837888876761), (1772, 0.004003333399430373), (1559, 0.003992703732862145), (1699, 0.003991474843652324), (4426, 0.003980631223261024), (234, 0.003970509617032526), (3339, 0.003970201087966742), (625, 0.0039700919528630274), (1546, 0.0039687964989061015), (1753, 0.003965524253339128), (2801, 0.003957482166523577), (3776, 0.00395109019216415), (1309, 0.003948380480033668), (1120, 0.003933222812334196), (3405, 0.003921088336881911), (2541, 0.003914935281133384), (723, 0.003905451704110582), (1458, 0.003904651594659914), (1910, 0.003897392208484155), (639, 0.003895629946806929), (3806, 0.003891967785171729), (3512, 0.003889013171202378), (2757, 0.0038818149563784156), (314, 0.00386727864603967), (640, 0.003862120234585781), (3484, 0.003836623982975266), (4555, 0.003822393043576866), (4513, 0.003816259526860173), (469, 0.0038125681688557884), (2998, 0.003807469070934451), (738, 0.00380050542824053), (2573, 0.0037816412403020687), (3925, 0.0037750382833963), (290, 0.0037646025269972177), (76, 0.0037642771162936252), (295, 0.0037622811700992434), (1164, 0.0037512621307350573), (3944, 0.003718810489424915), (3989, 0.0037165667421229062), (1395, 0.0037135203999899623), (289, 0.003702706209227987), (1576, 0.0036952051361189295), (4607, 0.003682819782953627), (2529, 0.0036815468729244245), (294, 0.0036732829549063557), (2078, 0.0036690612024628845), (2379, 0.0036601865946633357), (2490, 0.003655433841287204), (2937, 0.0036418513127225525), (3523, 0.003635675158808224), (4705, 0.0036260817428888804), (2326, 0.0036225713051403125), (3051, 0.003617701658361142), (2764, 0.003613273940570898), (3672, 0.003603859110894286), (2858, 0.003594793230747527), (2137, 0.0035945925620135804), (3139, 0.0035907551640025526), (4082, 0.00358280122205307), (2722, 0.0035603643441040962), (2189, 0.0035601273816176465), (4202, 0.003546305715914872), (3040, 0.003541823977779952), (2989, 0.003533948201952056), (2251, 0.003528765524922965), (3166, 0.0035179839931373026), (2349, 0.003511569740426779), (1145, 0.0035070545267648348), (2407, 0.003505785923314623), (3990, 0.003500660434369241), (2889, 0.003491315543824116), (2537, 0.0034791458040229705), (77, 0.003476980872095499), (4704, 0.003464734517458659), (3052, 0.003464159943233294), (735, 0.003463159634339838), (3055, 0.0034510966937722886), (2404, 0.0034495650395905005), (2775, 0.003443022569045042), (4017, 0.0034416299225726275), (2870, 0.0034381012735800014), (3561, 0.003438052370675986), (3042, 0.0034363661000082163), (3030, 0.0034357627126280015), (627, 0.0034341999825618446), (2883, 0.003432062958059232), (2923, 0.003417166947221909), (3291, 0.0034081886534521894), (2731, 0.003404339062511265), (4749, 0.0034036456368132157), (4222, 0.0034013828055934094), (4529, 0.0034005010522372646), (2310, 0.0033909407420161346), (4221, 0.003390872397994604), (3479, 0.0033870072429741257), (4484, 0.0033814476312483683), (4611, 0.0033805137878272673), (3939, 0.0033779025927503665), (2673, 0.0033738107663759957), (2861, 0.003361654585292839), (1210, 0.0033546679070800924), (4172, 0.0033528725699006785), (2559, 0.0033339816446641937), (3878, 0.0033333249663985306), (4418, 0.003330912615368857), (2832, 0.003328358371392943), (4696, 0.0033226057436817526), (2628, 0.0033200750239033732), (4407, 0.003317390193547925), (3219, 0.003314404248274218), (2448, 0.003312180628444434), (2392, 0.0033114422157635385), (3292, 0.0033107771042186927), (3762, 0.00330411757499818), (2199, 0.003301396132983232), (3892, 0.0032969468162486887), (3282, 0.0032890614008540533), (4423, 0.003288729379767851), (4019, 0.0032877144876280353), (2425, 0.003286983090237742), (2643, 0.003280052907901832), (2257, 0.003265288941763766), (3322, 0.0032640971868044587), (889, 0.003263982140942741), (3262, 0.0032633245940029516), (2350, 0.00325898047079926), (2901, 0.003256227513237159), (4230, 0.003249625623118119), (4142, 0.0032425169740557275), (2838, 0.0032411818306879335), (2286, 0.0032411344327654677), (1153, 0.0032346284116908913), (1208, 0.003233402541827205), (4400, 0.00323306097982072), (4102, 0.0032201764133058803), (3848, 0.0032176256582615117), (3015, 0.0032138288529427426), (4606, 0.0032107990543004962), (3239, 0.0031975367271760966), (3128, 0.003197007951514602), (2423, 0.003196216137743943), (3354, 0.0031930841877435712), (3140, 0.003191775106003641), (526, 0.0031892059612266465), (475, 0.003183017020864471), (1711, 0.003180428719665651), (1121, 0.0031774370506779245), (3687, 0.0031677160464612685), (4692, 0.0031658445386857584), (4521, 0.0031656248700788828), (4544, 0.003163843742069543), (3363, 0.003163022311998248), (3616, 0.003153843318530539), (3357, 0.0031524982659526623), (2834, 0.00314646446990567), (3537, 0.0031457463849610887), (2557, 0.003145443106586993), (2438, 0.003141434949500873), (3159, 0.003138905401171387), (3429, 0.0031366553343255815), (4306, 0.0031355357755684875), (3577, 0.003134300423040642), (4107, 0.0031316484334973902), (3922, 0.0031308493874409268), (2857, 0.0031306293625923613), (3613, 0.0031282114428502436), (2266, 0.0031228492472702065), (4572, 0.0031126376024216505), (3074, 0.0031116199020941445), (4298, 0.0031114236658140513), (326, 0.003105938774714085), (2797, 0.003104258374734227), (2957, 0.0031027576887766853), (3874, 0.0031013363262410347), (4723, 0.00310090615463497), (2488, 0.0030994924411226936), (3031, 0.003098080340964135), (3832, 0.003096146879951484), (2848, 0.0030957310537843), (3302, 0.003090102959529381), (3620, 0.0030882893020226327), (4147, 0.0030881294441047137), (3544, 0.0030871824814445417), (2966, 0.003083110206798772), (3358, 0.0030790201365820634), (3020, 0.0030788992114505528), (2415, 0.0030774782113262584), (1593, 0.003073536197767713), (3206, 0.003068521345130194), (2454, 0.0030625130786813577), (2993, 0.003059036294957494), (3257, 0.003055972375457137), (2619, 0.0030541950397158135), (777, 0.003048206537715965), (3413, 0.0030462569383745484), (1168, 0.0030455201632660664), (2895, 0.003035734397694937), (489, 0.003033907649847658), (2434, 0.0030319578792125535), (3911, 0.00303052451245541), (4458, 0.003024789988948817), (1049, 0.0030073286045681187), (4280, 0.0030057193500140156), (2772, 0.003004298617678023), (3308, 0.0030025452049455338), (2986, 0.0029999075948067633), (4717, 0.0029946805054474088), (2738, 0.002992961118255661), (431, 0.0029909808972183064), (4632, 0.0029900152728193187), (3763, 0.002988962008197595), (3935, 0.0029885096547979943), (2613, 0.002987833615753465), (4416, 0.0029853335777020916), (2570, 0.002985006527074178), (3081, 0.002984739096348554), (2378, 0.002984702466710939), (3621, 0.0029843451284689345), (3745, 0.002983416534820059), (4584, 0.0029816502268501864), (4633, 0.0029805712061734815), (1792, 0.002980454256720252), (4694, 0.0029799396515033144), (1187, 0.002979770691711471), (4145, 0.0029791881546168577), (2707, 0.0029766094818745683), (518, 0.0029732402429394856), (2720, 0.0029724638078420245), (1748, 0.002969346654113988), (4030, 0.0029685098507899778), (4589, 0.002968495055423245), (1169, 0.002968248475121234), (4075, 0.002959310749705171), (3540, 0.0029580551139992647), (2142, 0.002957911816921575), (1547, 0.0029538683671561368), (3359, 0.0029515322197334465), (4126, 0.0029512048892630515), (2544, 0.002950977553805173), (3884, 0.0029508011050974983), (2320, 0.0029483683178666044), (2696, 0.0029482119642483444), (3072, 0.0029477207530535492), (3307, 0.0029460254497445243), (4002, 0.0029453637825473953), (1947, 0.002944168345871454), (2269, 0.0029435278244624215), (2924, 0.002941313927795408), (3754, 0.00294123732407041), (3729, 0.002939207932414357), (3425, 0.002938660148668835), (4713, 0.0029359206463355366), (3230, 0.0029279919041756575), (2987, 0.0029279224859267345), (3364, 0.0029277933783362665), (2884, 0.002927723897692589), (448, 0.0029273791170721856), (3419, 0.002926833737465544), (3337, 0.002926360855104773), (3396, 0.002925354196686554), (3506, 0.002925090773173954), (3866, 0.0029234354102327348), (4650, 0.0029227923349272288), (2872, 0.002919385177617543), (4369, 0.0029178234754435894), (3355, 0.0029177922097563735), (925, 0.002916183387409237), (508, 0.0029161753848960135), (4507, 0.002913088748170219), (3165, 0.0029129982157773643), (4267, 0.0029122220382451474), (2478, 0.002911461177243871), (614, 0.00290989792253315), (3952, 0.002908452739992948), (4516, 0.0029082392469185234), (1656, 0.0029077079992601354), (3639, 0.0029025843465260875), (2796, 0.002902421975777824), (3651, 0.002901290672648267), (985, 0.002901203439820041), (2702, 0.0028986752398810866), (4295, 0.0028956476258980364), (4117, 0.0028951057091739976), (1497, 0.00289446576555683), (739, 0.002894012255446743), (4753, 0.0028919487884017663), (4243, 0.0028872437447467303), (3772, 0.0028861665077737704), (3296, 0.0028845687282931273), (2223, 0.002883657739557414), (3611, 0.002881671319418458), (2302, 0.0028806560860410685), (2629, 0.0028789827889471042), (2437, 0.0028786888060857926), (1909, 0.0028786576539522103), (3186, 0.002875686598671847), (998, 0.002875096610449085), (1887, 0.0028740961062598642), (999, 0.0028727435442566034), (2411, 0.0028718128480025207), (3148, 0.0028715022964075974), (2623, 0.0028711452225422974), (478, 0.0028703090546665397), (2400, 0.0028685555016257766), (2914, 0.002868252351944781), (235, 0.0028626037655011655), (3013, 0.0028610165731193576), (576, 0.002858999118369583), (1349, 0.00285762811025138), (3274, 0.0028575753057830207), (3587, 0.0028569324986325506), (419, 0.0028564076731825015), (4368, 0.002854344086319595), (4333, 0.0028538356132755452), (3560, 0.0028496344498493186), (813, 0.0028484923414636154), (3962, 0.002848391112204595), (2974, 0.002847448826702877), (922, 0.00284543190818928), (4718, 0.002844408783172781), (596, 0.002841667503161745), (2916, 0.0028408048332358568), (1862, 0.0028404195325150506), (1594, 0.002839568084275876), (3414, 0.0028389857733314592), (4535, 0.0028386710230197294), (2134, 0.0028368228829513896), (308, 0.002836039428752784), (2356, 0.002835167909469329), (4401, 0.002833596125018068), (3737, 0.0028319594615577055), (3593, 0.0028311413543016003), (4051, 0.0028294868139303216), (3804, 0.002829137270933287), (1474, 0.0028283790706451106), (444, 0.002825858774682473), (3877, 0.002823766391590152), (3273, 0.00282353327570058), (2585, 0.002823318914999516), (2830, 0.0028226149209496683), (4397, 0.0028225842511361253), (41, 0.0028220612513682524), (4706, 0.00281767098412393), (3003, 0.002817373993822036), (4259, 0.0028171123677211895), (4113, 0.0028169590729902245), (2108, 0.0028149681631918447), (1890, 0.002814173123132308), (1109, 0.002812253640075932), (3062, 0.0028117656637352906), (4138, 0.002811175665091937), (2535, 0.0028109713012137647), (2592, 0.0028077159504372807), (3967, 0.0028036445992062004), (3026, 0.002802065432959627), (3101, 0.002801975252648181), (4042, 0.0028011681307968453), (857, 0.0028006579787448836), (2176, 0.002799738652446759), (1580, 0.0027985796143798237), (2890, 0.0027985606578063223), (2159, 0.002796642519650155), (4263, 0.0027933745595439814), (3417, 0.0027933086614350885), (587, 0.002789246217675594), (3116, 0.0027869581898004835), (476, 0.0027839829553150115), (3677, 0.0027839214224453152), (2410, 0.0027822668653526748), (4446, 0.002782149984041176), (1479, 0.0027816518653624054), (4308, 0.0027812821125682), (1733, 0.00278081968063316), (2390, 0.00278029308266928), (3183, 0.002777237875199438), (2624, 0.002775130272788046), (253, 0.0027728619056607952), (3234, 0.002772188328120311), (3714, 0.002772130097690375), (4130, 0.0027720301380200125), (318, 0.0027716213992394355), (4140, 0.002771074176592469), (3497, 0.0027710447255302117), (4101, 0.0027681114618960017), (3813, 0.002767235426300998), (4732, 0.0027662301144192277), (3749, 0.002765280753409115), (1905, 0.002765022738371266), (3044, 0.002764551763558158), (2293, 0.0027644911596349914), (1805, 0.0027632161822077734), (499, 0.002760042990982669), (3064, 0.0027596699778360194), (2748, 0.0027578844179992276), (3258, 0.0027578268313340052), (887, 0.0027576749224545974), (4087, 0.002757014892292607), (2882, 0.0027559720055843886), (2507, 0.002755050857258632), (3915, 0.0027547260209605175), (8, 0.0027543335470164663), (4528, 0.0027542947624417113), (2595, 0.0027508174308408452), (3889, 0.0027505286173344057), (2888, 0.0027472806692475423), (2705, 0.0027461280207631174), (4545, 0.0027445443902041006), (1959, 0.0027434360138272663), (3269, 0.0027434131677741983), (192, 0.0027430559563033185), (4734, 0.0027408297226725643), (3449, 0.00274058636453638), (3271, 0.0027403415978842337), (3893, 0.0027398348303490174), (4024, 0.002738817823037397), (3757, 0.0027358120658869957), (2190, 0.0027337675859246567), (2776, 0.0027315257028121924), (1518, 0.0027314707555649094), (1848, 0.0027301751429851424), (1907, 0.0027299453987985325), (4132, 0.002729915146874504), (4161, 0.0027284295702252356), (4657, 0.00272766942235733), (2475, 0.0027274386737216644), (1995, 0.0027271106496794184), (4540, 0.0027251255860746932), (4245, 0.0027249016733194827), (791, 0.0027245490827624776), (3184, 0.002724037993344761), (2661, 0.0027225967815229855), (3496, 0.002722348105245073), (395, 0.00272106521247246), (1637, 0.002720463657139302), (4269, 0.0027203946975308474), (3781, 0.0027174020257633258), (4495, 0.002716533945847962), (2786, 0.002715966686361918), (4574, 0.002715543513395254), (872, 0.0027151279537172817), (4111, 0.0027150310497208023), (1683, 0.0027139443671448764), (1409, 0.0027132641602936663), (2260, 0.002713062173204411), (2725, 0.002712359055125161), (3873, 0.0027118935084019494), (4680, 0.0027116711744928136), (2940, 0.002710772343352202), (3007, 0.002709427775494519), (2391, 0.0027087775163753196), (12, 0.002708340354961457), (2393, 0.0027065538121768627), (1324, 0.002705358234925375), (2609, 0.0027051460174360585), (826, 0.002704815148187846), (3601, 0.002704796924602712), (2664, 0.002703826942826442), (3235, 0.002703665113092289), (4357, 0.0027034679302635803), (2970, 0.0027032949511497564), (4355, 0.0027018875230114072), (4169, 0.0027015747367255603), (3987, 0.0027012118924889077), (2105, 0.0027006582225229704), (3434, 0.0026981585993175548), (3678, 0.0026980940701351206), (74, 0.002697321222497816), (680, 0.0026971854142241744), (246, 0.002697163563809614), (3590, 0.0026940584214214624), (623, 0.0026936257054534724), (612, 0.0026927305201672825), (2821, 0.002692429842320299), (1896, 0.002690520691747851), (2361, 0.0026901282387533547), (3084, 0.0026899001407307507), (4489, 0.0026898571212910427), (3314, 0.0026898098056917486), (4471, 0.002689451482618859), (4054, 0.002689240504457996), (456, 0.002687049016489072), (2792, 0.0026869471767721692), (4505, 0.0026845407116629577), (2953, 0.002684490889512162), (4575, 0.002683455745897461), (2288, 0.002682616857696323), (2755, 0.0026817901026760537), (4286, 0.0026814309883877183), (2610, 0.0026802854429516182), (4318, 0.00267995282520947), (1822, 0.002677246887881095), (3037, 0.0026770809629725915), (3406, 0.0026765700485092483), (4, 0.0026759665928032302), (1893, 0.002674980291477653), (4420, 0.002674280774418094), (4566, 0.0026735546109579985), (2878, 0.0026734722698293838), (1916, 0.0026726151622681773), (3388, 0.002672146305255844), (783, 0.002671657768184265), (2385, 0.0026712362062835497), (1007, 0.0026699680308093048), (1670, 0.0026693561451880065), (3882, 0.002669225472758663), (3187, 0.0026688975569496218), (178, 0.002667965049488923), (3654, 0.002667297611504451), (1570, 0.0026672319410395466), (2419, 0.002664517725272706), (262, 0.0026643359555147046), (3372, 0.002663590840347564), (3242, 0.0026627240239371097), (4225, 0.002662303167849778), (1402, 0.002659466738009274), (564, 0.002657027849458249), (4363, 0.002656280498809686), (1439, 0.0026554823490857376), (4497, 0.0026552611205088346), (3493, 0.0026545144823408597), (2083, 0.0026541513520933206), (3150, 0.0026535302094216734), (20, 0.0026527570934446066), (2926, 0.0026523761741113687), (3770, 0.0026521310442793435), (211, 0.0026509436265181466), (1660, 0.0026498822019617014), (4448, 0.0026486240455653193), (4083, 0.002647802731253027), (2561, 0.0026459399529272696), (3241, 0.0026458927031980622), (3845, 0.00264536067742802), (890, 0.0026450709873933557), (717, 0.0026448136161407753), (4419, 0.0026439719893291574), (2531, 0.0026431568888262663), (23, 0.0026429172195160193), (2370, 0.002642265734795532), (4136, 0.002642025728427912), (3224, 0.002640477416532266), (1851, 0.0026403793617911795), (2911, 0.002639526247691848), (3902, 0.0026388324543919197), (884, 0.0026386594931607945), (4361, 0.0026386334816726476), (2904, 0.002637905178614227), (2405, 0.0026377860013835812), (3353, 0.0026367027726778495), (588, 0.0026354138296516643), (2319, 0.0026346960439084625), (1364, 0.002633462452635989), (4625, 0.0026333505042846904), (4262, 0.0026330476415983117), (4756, 0.002632461050300673), (987, 0.002630563204847358), (4079, 0.002629117011058859), (2148, 0.0026287367207624723), (2072, 0.0026280155284696), (3920, 0.0026269850198830523), (11, 0.0026263170118314906), (3517, 0.0026259815785324952), (1703, 0.002624080641588584), (1765, 0.002623080121500158), (4340, 0.0026230583862476183), (3527, 0.0026216332494819416), (4334, 0.0026212769553910806), (4422, 0.0026208834421524514), (4287, 0.0026201914461210334), (3198, 0.002619974529864259), (2863, 0.002614997779838141), (3636, 0.002613638129283211), (377, 0.002613134236024629), (1717, 0.002611987036217893), (1516, 0.0026119169121049377), (3290, 0.0026100030058059252), (4643, 0.0026087964121890832), (1768, 0.0026075507565416424), (1946, 0.002606154682344158), (871, 0.002605879108742159), (2466, 0.0026046209947012903), (2230, 0.0026046209600846023), (865, 0.0026041473034027975), (3016, 0.0026036229481642107), (1294, 0.00260356810870273), (2894, 0.0026026276553647375), (4563, 0.0026006699960084098), (3289, 0.002599146485402696), (3225, 0.002598945361261664), (3809, 0.002598493390633651), (71, 0.002598233031967091), (3445, 0.002597374923532215), (1355, 0.0025971791308945563), (3526, 0.002595503472085825), (4273, 0.0025953107452440383), (3542, 0.002594891823392815), (115, 0.002593300200593264), (2386, 0.00259294748990694), (933, 0.0025901424197287393), (1176, 0.0025888535739499907), (969, 0.002588635847946133), (3113, 0.0025867747290768866), (3606, 0.002585895851771812), (4197, 0.0025854969931686654), (2073, 0.002584790940607842), (3182, 0.0025835580046934636), (3283, 0.0025832882921760798), (2292, 0.0025830825071317524), (1122, 0.0025820607421187945), (3707, 0.0025812562026774188), (2397, 0.002579374719519521), (3792, 0.0025791715630782298), (2746, 0.0025787071567579885), (2313, 0.0025749114546800315), (4049, 0.002573949972108381), (198, 0.002573256321933336), (1204, 0.002573206584190331), (2430, 0.002573152120809181), (1533, 0.0025726575647058076), (4135, 0.0025721544003564083), (579, 0.002570927431235828), (1476, 0.002569492630955095), (4014, 0.0025661071943593977), (3739, 0.0025640637911042356), (2652, 0.002563989720311715), (1410, 0.0025632853630778354), (4391, 0.002563059388397236), (3335, 0.0025624988480590443), (4501, 0.0025623314809338042), (1722, 0.0025610950655021386), (3551, 0.0025597255630833856), (1574, 0.0025593435180176335), (1706, 0.002559280265609513), (2396, 0.0025592317330554275), (4266, 0.002559182443926289), (2554, 0.002558519538702846), (848, 0.002557744428375922), (993, 0.002554833899416498), (2192, 0.0025540715080322415), (2169, 0.0025525752827928266), (2783, 0.002552340094267794), (2492, 0.0025520544443002457), (4686, 0.002551643339660422), (504, 0.002551508415229109), (2067, 0.0025514295143559346), (2533, 0.0025508245122476576), (4604, 0.0025498804584698246), (2826, 0.002549723716021327), (378, 0.002547043242925245), (3491, 0.002546138032500976), (3564, 0.0025460210758847046), (1131, 0.002544645217036425), (3341, 0.0025432834702508117), (2340, 0.002542464113880335), (1170, 0.002539030797647179), (2354, 0.002538709830463113), (114, 0.002538593432573124), (749, 0.002537705888891391), (4330, 0.00253759563114658), (1304, 0.0025370239986737347), (3478, 0.0025361871902406415), (2495, 0.0025359570773834284), (226, 0.0025358335946023417), (1378, 0.0025340273053027075), (4427, 0.002533334775450861), (1163, 0.0025317112602762436), (66, 0.0025312341363153924), (2387, 0.002530666096103633), (4320, 0.0025297404552931534), (2195, 0.0025294940131200027), (2900, 0.002528116234955642), (2943, 0.0025270661897384182), (3673, 0.0025259098893481075), (3216, 0.002523810162634958), (2853, 0.0025234742839204257), (4056, 0.0025224767280474544), (1298, 0.0025221305830124743), (2999, 0.0025217999584430033), (4409, 0.0025211780579558235), (2289, 0.0025186187714120985), (4394, 0.002516685249546862), (3441, 0.0025153505923608713), (3477, 0.002514868609303398), (1891, 0.0025141756377858905), (400, 0.00251289546460505), (1072, 0.002511969113336023), (490, 0.0025114046023391725), (4520, 0.00251065636202738), (348, 0.0025106049309844727), (2060, 0.0025104283919120114), (3565, 0.002509988657408572), (1831, 0.0025076495173526085), (247, 0.002507649315273456), (466, 0.002507384990996102), (1411, 0.0025061728502699713), (2569, 0.0025060501697395116), (3381, 0.002505897357895813), (4228, 0.002505610963151872), (1598, 0.002503578013704265), (1666, 0.0025010320929579662), (1550, 0.002500843149361938), (2416, 0.0024995988683299913), (1313, 0.0024991701666688348), (973, 0.0024986829749220254), (4487, 0.002498674942563265), (3173, 0.0024976685366919467), (3093, 0.0024959578802307074), (2946, 0.0024959286076673085), (3906, 0.002495287660533279), (3647, 0.0024952762541183417), (1100, 0.002494207439481666), (1110, 0.0024929035561424492), (169, 0.002491783750451106), (215, 0.002491610501274281), (1026, 0.0024886894329191793), (1319, 0.0024882460941023266), (4020, 0.0024881089755816052), (3557, 0.0024870467081049524), (3827, 0.002486666559187951), (3379, 0.0024864932425056924), (1286, 0.0024863444285309457), (1084, 0.0024851270070419744), (1882, 0.002484915947496337), (2111, 0.002484294204794003), (98, 0.00248340938176191), (2945, 0.0024825994654153038), (26, 0.0024815199490618002), (4530, 0.002480367673515684), (2226, 0.0024799385815856712), (4687, 0.0024798705471827), (3220, 0.002478699076060922), (4036, 0.002478077422724702), (3069, 0.0024767080275248632), (1617, 0.0024759756901920225), (3719, 0.0024754549920114216), (3706, 0.0024751333238974306), (4743, 0.002474603104085691), (3412, 0.002473500072167002), (2909, 0.002473493900684701), (3402, 0.0024714558599442256), (1350, 0.002470461927847056), (1408, 0.0024700615971213528), (127, 0.0024694587388694603), (1422, 0.0024693633273359873), (1284, 0.002468849236494781), (2401, 0.002464829336269373), (755, 0.0024647317404651358), (3765, 0.0024636042749015424), (4693, 0.0024635743266324837), (959, 0.0024634028936061187), (3075, 0.002463151112658168), (1813, 0.002462243478839766), (2422, 0.0024618756983894995), (4183, 0.0024598501729012844), (349, 0.0024597751017132285), (2461, 0.0024590433491334033), (4381, 0.002458728622652153), (4550, 0.0024586748500938596), (4573, 0.002458614741936614), (4129, 0.0024548456995279735), (3348, 0.002454413673103588), (3890, 0.0024536526556442157), (541, 0.0024531262551875303), (488, 0.002453124966462652), (4472, 0.0024516055231321734), (2571, 0.0024503212988856386), (1645, 0.0024501016352676042), (3298, 0.002449889141972864), (4069, 0.0024496794215734174), (1247, 0.002449604610534502), (2612, 0.0024494145037263775), (2268, 0.002449391524423003), (3641, 0.0024493907161684263), (4139, 0.0024490787046745617), (1969, 0.0024475444749093773), (1463, 0.0024452807156080236), (2642, 0.0024435014093075946), (1597, 0.0024430773578123536), (4461, 0.0024415519508728914), (3917, 0.0024396790123713268), (646, 0.0024389251045113143), (3900, 0.002438771217157476), (1117, 0.0024363948721887476), (2131, 0.0024363566535109513), (4729, 0.0024361362289319404), (2117, 0.002432738926313127), (3503, 0.0024319481504375285), (1034, 0.0024287885484453667), (487, 0.0024278315922302163), (2367, 0.0024277017381169885), (731, 0.002426041885645131), (1027, 0.002425178530119394), (2141, 0.00242412156867798), (4567, 0.0024239308498221444), (1416, 0.0024236082196454393), (4536, 0.0024230497488252263), (4155, 0.0024229225872662036), (883, 0.002422689099820759), (3214, 0.0024212685427485426), (2779, 0.0024210805376161204), (3268, 0.0024206147492601745), (854, 0.0024204130433707048), (798, 0.002420279154987218), (1877, 0.002420130506591283), (1744, 0.002419466647815223), (1929, 0.0024177987312427804), (1002, 0.0024164625079969525), (3390, 0.0024164444715753866), (157, 0.002415439486141447), (4085, 0.002413872752453439), (1273, 0.00241372964489964), (3691, 0.0024132941512466618), (3170, 0.0024127694654795177), (984, 0.0024124304913493468), (4213, 0.002411633257182007), (221, 0.002411361490287575), (2765, 0.0024107410707284744), (2242, 0.0024106327127107344), (2068, 0.0024099656054347002), (505, 0.002409323202911005), (2965, 0.0024091872105101776), (4206, 0.0024090792775228152), (4428, 0.0024082352367095087), (2892, 0.0024074500325428775), (3898, 0.0024067454994173855), (767, 0.002405830891505593), (4345, 0.0024056806139171995), (3799, 0.0024040976357289317), (373, 0.0024035937816996485), (2679, 0.002399906962190324), (698, 0.002399544762154424), (2651, 0.002399527090955675), (3646, 0.002398125884687227), (1742, 0.002398036686183952), (1404, 0.0023973664832842947), (2997, 0.0023971601065590838), (325, 0.002396607136979531), (2800, 0.002396136918108817), (1032, 0.002395440149663579), (3014, 0.0023942259924392586), (388, 0.0023942044323020653), (3194, 0.002393826048162591), (1036, 0.002391995314691645), (3811, 0.0023908909837663888), (1663, 0.0023892673771611765), (2166, 0.002388531571930009), (3615, 0.002388296766524122), (2525, 0.0023881792409710723), (2004, 0.0023836845211184176), (3300, 0.0023833694605941173), (4011, 0.0023818585917991975), (507, 0.0023814032611240723), (4254, 0.002381355869945804), (1693, 0.00238125826288348), (154, 0.002380610004741567), (3057, 0.0023791981149129493), (1372, 0.002379092284915241), (886, 0.002377685816062925), (140, 0.0023757143815839364), (3071, 0.0023755248561706534), (941, 0.0023753858347316313), (3243, 0.0023753766953138553), (975, 0.002374254485406639), (4059, 0.0023717520410445306), (2552, 0.0023711683412701526), (2099, 0.002370514864288073), (1884, 0.0023704895535816193), (2634, 0.0023697651035010894), (471, 0.002368427181806095), (655, 0.0023683578516378546), (4634, 0.002366537186237376), (229, 0.002364464894441411), (2862, 0.00236358722606658), (372, 0.0023630726175345187), (598, 0.002363017019179979), (944, 0.002362909437140335), (659, 0.0023624315239011303), (3725, 0.0023614834077740256), (3147, 0.0023610495805435113), (410, 0.0023595146802160606), (2201, 0.002359272840430378), (4356, 0.002358670992777147), (1558, 0.0023575804558839345), (2446, 0.0023555939250982988), (2528, 0.0023552329351234197), (1456, 0.0023540541645859295), (3500, 0.002352966728399302), (2907, 0.0023521461999904784), (1641, 0.0023518531695646367), (2556, 0.0023516975035823683), (589, 0.0023504596104199846), (2129, 0.002350041367477206), (399, 0.0023500375059201137), (1642, 0.002347271044462082), (2317, 0.002346650633681952), (3627, 0.002346613265148603), (805, 0.0023452728300887567), (4616, 0.0023428090596489324), (136, 0.002342053663543897), (2735, 0.002341654335424115), (2399, 0.0023410933373043154), (2593, 0.002339930796183013), (3369, 0.0023393798748198896), (355, 0.002338600461277963), (2482, 0.0023377306593093767), (324, 0.0023375564513999506), (1357, 0.0023372106844995522), (1543, 0.0023366207244844292), (4479, 0.0023358563951205434), (1814, 0.002335195713558715), (2674, 0.002334618638576613), (4174, 0.0023343493902812707), (2845, 0.0023343307734320145), (4348, 0.0023323300386728536), (907, 0.002332300601765917), (1079, 0.0023322559654003526), (2453, 0.002330973019391161), (121, 0.0023309647694089563), (3455, 0.0023287089983759627), (457, 0.002327732812904547), (359, 0.0023274681266520665), (524, 0.002326628494390853), (4326, 0.0023252246844545858), (416, 0.002324088327746965), (3050, 0.002323618032452493), (4277, 0.0023230286175405803), (1672, 0.002321722396026475), (1628, 0.0023205936685129582), (624, 0.0023197786136598814), (1782, 0.0023196197449962324), (4620, 0.00231727195620905), (3742, 0.002316604456287793), (2954, 0.002315748814608356), (1434, 0.0023155273672975777), (4359, 0.002315457705635693), (4638, 0.0023135084446129625), (3563, 0.0023114996233486447), (759, 0.002309117906857392), (2728, 0.0023085003156347404), (3953, 0.0023075672917894073), (3278, 0.002306109060903631), (1528, 0.002303568038250878), (1503, 0.00229947342488938), (2402, 0.002296822088102547), (3304, 0.0022964795595691884), (1869, 0.0022962581361569956), (3614, 0.002295596338649645), (473, 0.0022945038896853643), (3311, 0.0022941875363447282), (1827, 0.002293422535226092), (1826, 0.0022933726714825576), (2338, 0.0022913946207671343), (1605, 0.0022912512467324424), (1161, 0.002289389845898506), (1719, 0.002288890438865886), (2323, 0.002288710033556969), (1366, 0.002287746831385266), (4350, 0.0022859700538679396), (4712, 0.0022846896996839036), (2741, 0.0022835488818161043), (1080, 0.002283153078480931), (3336, 0.0022827623066486316), (4074, 0.0022823850645029334), (3027, 0.0022822077528129765), (3986, 0.0022819497828374434), (2457, 0.002281400117753307), (1625, 0.0022805657073798956), (4143, 0.0022797552107130963), (3863, 0.0022790086794717717), (722, 0.0022788621644894975), (4304, 0.0022762430833830217), (2591, 0.002275344532719518), (1219, 0.002275219115804935), (158, 0.002274967685727569), (3327, 0.0022748666683518074), (1980, 0.00227477464899649), (1808, 0.002274528278954003), (4080, 0.0022740107861656984), (1004, 0.0022732257076968914), (2976, 0.0022719244680200154), (3795, 0.0022686851808269076), (594, 0.0022668822325154735), (1921, 0.00226658677711873), (815, 0.002265810207528326), (856, 0.002263834787264893), (2163, 0.0022629965639827504), (268, 0.0022620244651643815), (1318, 0.0022618699066821774), (2213, 0.0022616680757847943), (1392, 0.0022549171667648254), (703, 0.002252830558764676), (3380, 0.0022513613222782006), (1423, 0.002250838550875257), (132, 0.0022485035909542398), (1830, 0.002247218249834534), (1394, 0.0022470021552231235), (1954, 0.0022466176603640644), (1251, 0.0022442547715836978), (4343, 0.002243294059099312), (495, 0.0022431563403783133), (3755, 0.002241461077547312), (2047, 0.0022411341263223567), (712, 0.0022406993971376544), (2502, 0.00223764903510972), (4220, 0.0022373580615292327), (1199, 0.002237279405744827), (2753, 0.0022342808694140515), (184, 0.0022333195719391554), (92, 0.002231938202318901), (605, 0.0022316315763223366), (4247, 0.0022291096577025686), (1616, 0.0022287724411460983), (4066, 0.002227252098130379), (97, 0.002225672039651193), (2240, 0.0022256256462686403), (480, 0.0022254937857947676), (647, 0.002225248093371474), (3894, 0.0022242858410916593), (249, 0.0022242181571218047), (1301, 0.002215732627951938), (4296, 0.0022091218180194483), (4473, 0.0022088482857684994), (1943, 0.0022075058990114116), (2721, 0.0022037253425713542), (4429, 0.002202062550120158), (1217, 0.0022018181096331805), (2520, 0.0021985696707984234), (2747, 0.0021975775185931763), (103, 0.002196696924815654), (3211, 0.0021958742889033934), (165, 0.002192430843204887), (2270, 0.00219130592332667), (357, 0.0021885661052920605), (1828, 0.0021883753970884136), (4386, 0.00218734688146368), (1370, 0.002186813531333692), (1450, 0.0021855787670099175), (278, 0.0021843202599993133), (3238, 0.0021825937843072797), (2527, 0.0021813091911791218), (3393, 0.0021812533691201504), (286, 0.0021763451606793822), (2611, 0.0021758158812791722), (3569, 0.002174456030263495), (2743, 0.002174428378375937), (4411, 0.002172750642469467), (2382, 0.002172550292225871), (4476, 0.0021702148234961057), (1088, 0.002168028396331156), (1565, 0.0021678323941890097), (2146, 0.0021674057808973805), (1691, 0.002164018010334086), (432, 0.002157573346153142), (3200, 0.0021549128346638855), (1352, 0.0021543285954857753), (2758, 0.002153957079075249), (1340, 0.002153835131845671), (3855, 0.002151981507583706), (626, 0.0021492988165263674), (3669, 0.00214929577871008), (267, 0.0021492676003019005), (3668, 0.0021466768089874176), (951, 0.002141013818313958), (3657, 0.0021402453501994092), (4636, 0.0021387597745254486), (2039, 0.0021333513682361693), (707, 0.002133185976689703), (195, 0.0021317422811621754), (196, 0.002130241788619929), (1801, 0.002129912236167644), (2127, 0.0021291085789020394), (3347, 0.0021286521604270314), (2132, 0.002118807318914566), (3928, 0.002118505549736894), (1042, 0.0021181778347175257), (2359, 0.0021168368849086407), (2287, 0.002115909997010881), (1209, 0.0021134636228278113), (3252, 0.002113286442481704), (3056, 0.002101035489155866), (901, 0.0021006570803087372), (3024, 0.002098006477285881), (4200, 0.0020968865998536737), (1305, 0.0020966909382619018), (4015, 0.002092105915652035), (2034, 0.002089491496826586), (3548, 0.0020856240241655002), (2509, 0.0020841748846264375), (1427, 0.0020790061804810836), (1415, 0.002077914644244706), (2526, 0.0020750832006275386), (645, 0.0020714050466539096), (1624, 0.0020638114682631757), (4311, 0.00206051039801924), (4744, 0.002055966077073321), (2441, 0.002053736643431966), (4626, 0.002050481727273585), (3575, 0.0020489254243474405), (3431, 0.0020366287014385314), (194, 0.002034839745506438), (3538, 0.0020222667751278976), (2766, 0.0020124065471371724), (2010, 0.0020028590070789534), (1677, 0.001995311917545588), (4598, 0.001989708285475718), (3301, 0.0019860420011163526), (1040, 0.0019808664673990114), (3199, 0.0019640006274080314), (607, 0.00195429012036482), (3626, 0.0019457778288461563), (453, 0.0019393347333000763), (351, 0.001934949810470641), (228, 0.0019207863172057056), (2636, 0.0019040719219632182), (4445, 0.001903935600604458), (1277, 0.0018965691925550338), (3546, 0.0018921856768456724), (4301, 0.001881648020866405), (2902, 0.0018652926953995987), (4752, 0.0018166836686154622), (293, 0.0018032932320903585), (4171, 0.0017924201375203218), (3365, 0.0017885245766340776), (129, 0.0017710145837505121), (740, 0.0017013738490800241), (3392, 0.001685166142478692), (202, 0.0016641723699352556), (24, 0.0016564482636435309), (1780, 0.001654444868067222), (3608, 0.0016519407502508059), (2534, 0.0011313649045941105), (1, 0.0), (2, 0.0), (14, 0.0), (17, 0.0), (28, 0.0), (36, 0.0), (37, 0.0), (49, 0.0), (53, 0.0), (54, 0.0), (55, 0.0), (58, 0.0), (59, 0.0), (64, 0.0), (73, 0.0), (91, 0.0), (100, 0.0), (101, 0.0), (117, 0.0), (133, 0.0), (134, 0.0), (141, 0.0), (146, 0.0), (150, 0.0), (151, 0.0), (153, 0.0), (163, 0.0), (171, 0.0), (186, 0.0), (188, 0.0), (205, 0.0), (214, 0.0), (219, 0.0), (223, 0.0), (225, 0.0), (237, 0.0), (245, 0.0), (258, 0.0), (259, 0.0), (264, 0.0), (265, 0.0), (272, 0.0), (275, 0.0), (297, 0.0), (298, 0.0), (299, 0.0), (302, 0.0), (312, 0.0), (319, 0.0), (331, 0.0), (335, 0.0), (337, 0.0), (338, 0.0), (339, 0.0), (344, 0.0), (352, 0.0), (361, 0.0), (362, 0.0), (365, 0.0), (366, 0.0), (376, 0.0), (379, 0.0), (382, 0.0), (390, 0.0), (391, 0.0), (392, 0.0), (393, 0.0), (394, 0.0), (401, 0.0), (404, 0.0), (405, 0.0), (411, 0.0), (415, 0.0), (423, 0.0), (427, 0.0), (439, 0.0), (440, 0.0), (454, 0.0), (484, 0.0), (486, 0.0), (491, 0.0), (492, 0.0), (498, 0.0), (506, 0.0), (516, 0.0), (517, 0.0), (520, 0.0), (525, 0.0), (528, 0.0), (529, 0.0), (531, 0.0), (535, 0.0), (536, 0.0), (546, 0.0), (548, 0.0), (549, 0.0), (552, 0.0), (554, 0.0), (556, 0.0), (557, 0.0), (565, 0.0), (567, 0.0), (569, 0.0), (570, 0.0), (572, 0.0), (573, 0.0), (574, 0.0), (575, 0.0), (577, 0.0), (585, 0.0), (591, 0.0), (592, 0.0), (599, 0.0), (601, 0.0), (602, 0.0), (603, 0.0), (610, 0.0), (630, 0.0), (649, 0.0), (650, 0.0), (656, 0.0), (658, 0.0), (662, 0.0), (663, 0.0), (665, 0.0), (674, 0.0), (679, 0.0), (681, 0.0), (686, 0.0), (699, 0.0), (700, 0.0), (702, 0.0), (704, 0.0), (708, 0.0), (709, 0.0), (711, 0.0), (713, 0.0), (714, 0.0), (718, 0.0), (720, 0.0), (724, 0.0), (725, 0.0), (726, 0.0), (730, 0.0), (736, 0.0), (741, 0.0), (746, 0.0), (747, 0.0), (751, 0.0), (754, 0.0), (764, 0.0), (770, 0.0), (771, 0.0), (772, 0.0), (773, 0.0), (780, 0.0), (781, 0.0), (784, 0.0), (785, 0.0), (786, 0.0), (789, 0.0), (797, 0.0), (807, 0.0), (819, 0.0), (820, 0.0), (822, 0.0), (837, 0.0), (839, 0.0), (840, 0.0), (841, 0.0), (846, 0.0), (859, 0.0), (881, 0.0), (882, 0.0), (892, 0.0), (909, 0.0), (912, 0.0), (913, 0.0), (914, 0.0), (920, 0.0), (926, 0.0), (938, 0.0), (943, 0.0), (945, 0.0), (946, 0.0), (950, 0.0), (954, 0.0), (955, 0.0), (956, 0.0), (960, 0.0), (961, 0.0), (964, 0.0), (965, 0.0), (971, 0.0), (972, 0.0), (977, 0.0), (978, 0.0), (982, 0.0), (983, 0.0), (990, 0.0), (995, 0.0), (1008, 0.0), (1010, 0.0), (1011, 0.0), (1013, 0.0), (1016, 0.0), (1022, 0.0), (1025, 0.0), (1028, 0.0), (1029, 0.0), (1031, 0.0), (1038, 0.0), (1039, 0.0), (1051, 0.0), (1055, 0.0), (1056, 0.0), (1062, 0.0), (1066, 0.0), (1067, 0.0), (1073, 0.0), (1081, 0.0), (1086, 0.0), (1089, 0.0), (1091, 0.0), (1093, 0.0), (1097, 0.0), (1101, 0.0), (1103, 0.0), (1105, 0.0), (1106, 0.0), (1108, 0.0), (1113, 0.0), (1126, 0.0), (1130, 0.0), (1133, 0.0), (1135, 0.0), (1139, 0.0), (1142, 0.0), (1143, 0.0), (1147, 0.0), (1149, 0.0), (1151, 0.0), (1155, 0.0), (1156, 0.0), (1159, 0.0), (1165, 0.0), (1166, 0.0), (1171, 0.0), (1178, 0.0), (1180, 0.0), (1189, 0.0), (1190, 0.0), (1193, 0.0), (1196, 0.0), (1198, 0.0), (1200, 0.0), (1201, 0.0), (1212, 0.0), (1218, 0.0), (1221, 0.0), (1222, 0.0), (1227, 0.0), (1228, 0.0), (1233, 0.0), (1235, 0.0), (1240, 0.0), (1242, 0.0), (1244, 0.0), (1246, 0.0), (1253, 0.0), (1256, 0.0), (1258, 0.0), (1263, 0.0), (1265, 0.0), (1268, 0.0), (1269, 0.0), (1271, 0.0), (1285, 0.0), (1287, 0.0), (1288, 0.0), (1289, 0.0), (1291, 0.0), (1295, 0.0), (1296, 0.0), (1297, 0.0), (1299, 0.0), (1315, 0.0), (1321, 0.0), (1322, 0.0), (1323, 0.0), (1326, 0.0), (1328, 0.0), (1333, 0.0), (1336, 0.0), (1346, 0.0), (1353, 0.0), (1354, 0.0), (1368, 0.0), (1373, 0.0), (1390, 0.0), (1399, 0.0), (1424, 0.0), (1437, 0.0), (1441, 0.0), (1444, 0.0), (1447, 0.0), (1457, 0.0), (1459, 0.0), (1460, 0.0), (1466, 0.0), (1467, 0.0), (1468, 0.0), (1470, 0.0), (1473, 0.0), (1485, 0.0), (1487, 0.0), (1490, 0.0), (1491, 0.0), (1495, 0.0), (1496, 0.0), (1508, 0.0), (1511, 0.0), (1517, 0.0), (1520, 0.0), (1521, 0.0), (1522, 0.0), (1524, 0.0), (1525, 0.0), (1529, 0.0), (1532, 0.0), (1534, 0.0), (1535, 0.0), (1541, 0.0), (1545, 0.0), (1548, 0.0), (1549, 0.0), (1556, 0.0), (1557, 0.0), (1561, 0.0), (1563, 0.0), (1564, 0.0), (1569, 0.0), (1577, 0.0), (1578, 0.0), (1581, 0.0), (1584, 0.0), (1586, 0.0), (1589, 0.0), (1592, 0.0), (1596, 0.0), (1599, 0.0), (1600, 0.0), (1601, 0.0), (1602, 0.0), (1603, 0.0), (1604, 0.0), (1606, 0.0), (1607, 0.0), (1610, 0.0), (1611, 0.0), (1613, 0.0), (1615, 0.0), (1618, 0.0), (1626, 0.0), (1636, 0.0), (1638, 0.0), (1639, 0.0), (1640, 0.0), (1646, 0.0), (1649, 0.0), (1651, 0.0), (1668, 0.0), (1669, 0.0), (1673, 0.0), (1679, 0.0), (1686, 0.0), (1689, 0.0), (1697, 0.0), (1698, 0.0), (1700, 0.0), (1704, 0.0), (1709, 0.0), (1725, 0.0), (1726, 0.0), (1728, 0.0), (1729, 0.0), (1731, 0.0), (1734, 0.0), (1745, 0.0), (1751, 0.0), (1755, 0.0), (1756, 0.0), (1758, 0.0), (1766, 0.0), (1767, 0.0), (1769, 0.0), (1771, 0.0), (1775, 0.0), (1777, 0.0), (1778, 0.0), (1783, 0.0), (1785, 0.0), (1786, 0.0), (1794, 0.0), (1800, 0.0), (1803, 0.0), (1804, 0.0), (1810, 0.0), (1820, 0.0), (1823, 0.0), (1824, 0.0), (1825, 0.0), (1834, 0.0), (1835, 0.0), (1836, 0.0), (1839, 0.0), (1842, 0.0), (1844, 0.0), (1855, 0.0), (1856, 0.0), (1879, 0.0), (1883, 0.0), (1888, 0.0), (1889, 0.0), (1894, 0.0), (1898, 0.0), (1899, 0.0), (1912, 0.0), (1915, 0.0), (1917, 0.0), (1926, 0.0), (1928, 0.0), (1932, 0.0), (1938, 0.0), (1944, 0.0), (1955, 0.0), (1956, 0.0), (1961, 0.0), (1963, 0.0), (1965, 0.0), (1966, 0.0), (1972, 0.0), (1974, 0.0), (1978, 0.0), (1979, 0.0), (1984, 0.0), (2001, 0.0), (2002, 0.0), (2003, 0.0), (2006, 0.0), (2007, 0.0), (2009, 0.0), (2017, 0.0), (2019, 0.0), (2021, 0.0), (2025, 0.0), (2028, 0.0), (2030, 0.0), (2032, 0.0), (2033, 0.0), (2036, 0.0), (2038, 0.0), (2041, 0.0), (2042, 0.0), (2043, 0.0), (2046, 0.0), (2050, 0.0), (2054, 0.0), (2059, 0.0), (2063, 0.0), (2071, 0.0), (2079, 0.0), (2081, 0.0), (2085, 0.0), (2086, 0.0), (2090, 0.0), (2092, 0.0), (2106, 0.0), (2107, 0.0), (2115, 0.0), (2118, 0.0), (2120, 0.0), (2124, 0.0), (2125, 0.0), (2128, 0.0), (2135, 0.0), (2138, 0.0), (2140, 0.0), (2150, 0.0), (2152, 0.0), (2153, 0.0), (2164, 0.0), (2165, 0.0), (2168, 0.0), (2170, 0.0), (2171, 0.0), (2172, 0.0), (2179, 0.0), (2180, 0.0), (2182, 0.0), (2183, 0.0), (2186, 0.0), (2194, 0.0), (2200, 0.0), (2204, 0.0), (2215, 0.0), (2217, 0.0), (2218, 0.0), (2219, 0.0), (2220, 0.0), (2222, 0.0), (2225, 0.0), (2227, 0.0), (2233, 0.0), (2234, 0.0), (2238, 0.0), (2241, 0.0), (2243, 0.0), (2247, 0.0), (2249, 0.0), (2253, 0.0), (2256, 0.0), (2259, 0.0), (2261, 0.0), (2262, 0.0), (2263, 0.0), (2267, 0.0), (2271, 0.0), (2272, 0.0), (2274, 0.0), (2281, 0.0), (2282, 0.0), (2296, 0.0), (2297, 0.0), (2300, 0.0), (2305, 0.0), (2307, 0.0), (2311, 0.0), (2312, 0.0), (2315, 0.0), (2322, 0.0), (2325, 0.0), (2327, 0.0), (2329, 0.0), (2331, 0.0), (2332, 0.0), (2333, 0.0), (2337, 0.0), (2341, 0.0), (2342, 0.0), (2345, 0.0), (2351, 0.0), (2352, 0.0), (2357, 0.0), (2360, 0.0), (2364, 0.0), (2369, 0.0), (2372, 0.0), (2373, 0.0), (2377, 0.0), (2380, 0.0), (2381, 0.0), (2384, 0.0), (2389, 0.0), (2395, 0.0), (2398, 0.0), (2409, 0.0), (2414, 0.0), (2420, 0.0), (2431, 0.0), (2433, 0.0), (2435, 0.0), (2445, 0.0), (2450, 0.0), (2451, 0.0), (2452, 0.0), (2455, 0.0), (2456, 0.0), (2458, 0.0), (2462, 0.0), (2465, 0.0), (2470, 0.0), (2471, 0.0), (2472, 0.0), (2479, 0.0), (2483, 0.0), (2485, 0.0), (2491, 0.0), (2493, 0.0), (2497, 0.0), (2498, 0.0), (2499, 0.0), (2500, 0.0), (2504, 0.0), (2508, 0.0), (2511, 0.0), (2514, 0.0), (2515, 0.0), (2516, 0.0), (2518, 0.0), (2521, 0.0), (2523, 0.0), (2532, 0.0), (2536, 0.0), (2539, 0.0), (2542, 0.0), (2543, 0.0), (2547, 0.0), (2548, 0.0), (2549, 0.0), (2551, 0.0), (2562, 0.0), (2564, 0.0), (2566, 0.0), (2574, 0.0), (2575, 0.0), (2577, 0.0), (2578, 0.0), (2583, 0.0), (2584, 0.0), (2586, 0.0), (2588, 0.0), (2589, 0.0), (2590, 0.0), (2594, 0.0), (2596, 0.0), (2597, 0.0), (2604, 0.0), (2605, 0.0), (2608, 0.0), (2615, 0.0), (2616, 0.0), (2620, 0.0), (2627, 0.0), (2631, 0.0), (2637, 0.0), (2641, 0.0), (2648, 0.0), (2656, 0.0), (2657, 0.0), (2658, 0.0), (2659, 0.0), (2662, 0.0), (2663, 0.0), (2666, 0.0), (2667, 0.0), (2669, 0.0), (2670, 0.0), (2671, 0.0), (2672, 0.0), (2675, 0.0), (2676, 0.0), (2677, 0.0), (2681, 0.0), (2684, 0.0), (2685, 0.0), (2686, 0.0), (2690, 0.0), (2693, 0.0), (2701, 0.0), (2703, 0.0), (2704, 0.0), (2709, 0.0), (2715, 0.0), (2717, 0.0), (2719, 0.0), (2729, 0.0), (2730, 0.0), (2734, 0.0), (2737, 0.0), (2749, 0.0), (2750, 0.0), (2754, 0.0), (2756, 0.0), (2763, 0.0), (2770, 0.0), (2773, 0.0), (2781, 0.0), (2785, 0.0), (2793, 0.0), (2794, 0.0), (2799, 0.0), (2804, 0.0), (2806, 0.0), (2810, 0.0), (2811, 0.0), (2813, 0.0), (2814, 0.0), (2817, 0.0), (2818, 0.0), (2824, 0.0), (2827, 0.0), (2828, 0.0), (2829, 0.0), (2835, 0.0), (2836, 0.0), (2837, 0.0), (2839, 0.0), (2842, 0.0), (2850, 0.0), (2851, 0.0), (2852, 0.0), (2855, 0.0), (2856, 0.0), (2860, 0.0), (2864, 0.0), (2865, 0.0), (2866, 0.0), (2875, 0.0), (2877, 0.0), (2880, 0.0), (2891, 0.0), (2896, 0.0), (2898, 0.0), (2905, 0.0), (2906, 0.0), (2921, 0.0), (2922, 0.0), (2927, 0.0), (2928, 0.0), (2930, 0.0), (2938, 0.0), (2941, 0.0), (2951, 0.0), (2952, 0.0), (2955, 0.0), (2956, 0.0), (2958, 0.0), (2967, 0.0), (2968, 0.0), (2973, 0.0), (2979, 0.0), (2982, 0.0), (2983, 0.0), (2990, 0.0), (3001, 0.0), (3002, 0.0), (3006, 0.0), (3009, 0.0), (3021, 0.0), (3025, 0.0), (3029, 0.0), (3034, 0.0), (3038, 0.0), (3041, 0.0), (3047, 0.0), (3048, 0.0), (3054, 0.0), (3058, 0.0), (3059, 0.0), (3060, 0.0), (3061, 0.0), (3063, 0.0), (3073, 0.0), (3077, 0.0), (3078, 0.0), (3080, 0.0), (3082, 0.0), (3087, 0.0), (3088, 0.0), (3089, 0.0), (3090, 0.0), (3092, 0.0), (3103, 0.0), (3104, 0.0), (3105, 0.0), (3106, 0.0), (3107, 0.0), (3109, 0.0), (3115, 0.0), (3121, 0.0), (3130, 0.0), (3132, 0.0), (3138, 0.0), (3141, 0.0), (3145, 0.0), (3162, 0.0), (3169, 0.0), (3172, 0.0), (3175, 0.0), (3176, 0.0), (3177, 0.0), (3181, 0.0), (3188, 0.0), (3189, 0.0), (3190, 0.0), (3193, 0.0), (3197, 0.0), (3201, 0.0), (3202, 0.0), (3204, 0.0), (3207, 0.0), (3208, 0.0), (3212, 0.0), (3217, 0.0), (3221, 0.0), (3223, 0.0), (3229, 0.0), (3231, 0.0), (3236, 0.0), (3250, 0.0), (3251, 0.0), (3261, 0.0), (3266, 0.0), (3270, 0.0), (3272, 0.0), (3277, 0.0), (3281, 0.0), (3286, 0.0), (3287, 0.0), (3305, 0.0), (3310, 0.0), (3320, 0.0), (3321, 0.0), (3323, 0.0), (3324, 0.0), (3332, 0.0), (3333, 0.0), (3340, 0.0), (3343, 0.0), (3350, 0.0), (3366, 0.0), (3368, 0.0), (3371, 0.0), (3378, 0.0), (3383, 0.0), (3394, 0.0), (3397, 0.0), (3400, 0.0), (3401, 0.0), (3411, 0.0), (3415, 0.0), (3422, 0.0), (3424, 0.0), (3439, 0.0), (3442, 0.0), (3444, 0.0), (3454, 0.0), (3459, 0.0), (3461, 0.0), (3467, 0.0), (3472, 0.0), (3473, 0.0), (3475, 0.0), (3476, 0.0), (3481, 0.0), (3482, 0.0), (3485, 0.0), (3489, 0.0), (3490, 0.0), (3494, 0.0), (3505, 0.0), (3510, 0.0), (3519, 0.0), (3522, 0.0), (3525, 0.0), (3529, 0.0), (3530, 0.0), (3532, 0.0), (3533, 0.0), (3539, 0.0), (3543, 0.0), (3545, 0.0), (3547, 0.0), (3549, 0.0), (3550, 0.0), (3554, 0.0), (3562, 0.0), (3567, 0.0), (3568, 0.0), (3578, 0.0), (3581, 0.0), (3585, 0.0), (3589, 0.0), (3591, 0.0), (3592, 0.0), (3595, 0.0), (3600, 0.0), (3603, 0.0), (3607, 0.0), (3609, 0.0), (3610, 0.0), (3617, 0.0), (3622, 0.0), (3625, 0.0), (3628, 0.0), (3631, 0.0), (3633, 0.0), (3644, 0.0), (3649, 0.0), (3650, 0.0), (3662, 0.0), (3663, 0.0), (3671, 0.0), (3676, 0.0), (3681, 0.0), (3682, 0.0), (3683, 0.0), (3685, 0.0), (3686, 0.0), (3690, 0.0), (3693, 0.0), (3695, 0.0), (3697, 0.0), (3698, 0.0), (3700, 0.0), (3702, 0.0), (3703, 0.0), (3709, 0.0), (3712, 0.0), (3716, 0.0), (3717, 0.0), (3718, 0.0), (3722, 0.0), (3724, 0.0), (3726, 0.0), (3730, 0.0), (3732, 0.0), (3735, 0.0), (3736, 0.0), (3738, 0.0), (3740, 0.0), (3743, 0.0), (3758, 0.0), (3759, 0.0), (3760, 0.0), (3761, 0.0), (3764, 0.0), (3783, 0.0), (3785, 0.0), (3786, 0.0), (3789, 0.0), (3790, 0.0), (3791, 0.0), (3796, 0.0), (3798, 0.0), (3800, 0.0), (3803, 0.0), (3805, 0.0), (3808, 0.0), (3812, 0.0), (3816, 0.0), (3817, 0.0), (3818, 0.0), (3820, 0.0), (3830, 0.0), (3831, 0.0), (3834, 0.0), (3836, 0.0), (3837, 0.0), (3838, 0.0), (3840, 0.0), (3843, 0.0), (3846, 0.0), (3847, 0.0), (3851, 0.0), (3856, 0.0), (3858, 0.0), (3859, 0.0), (3869, 0.0), (3870, 0.0), (3879, 0.0), (3885, 0.0), (3887, 0.0), (3896, 0.0), (3912, 0.0), (3914, 0.0), (3918, 0.0), (3921, 0.0), (3929, 0.0), (3930, 0.0), (3931, 0.0), (3933, 0.0), (3936, 0.0), (3937, 0.0), (3943, 0.0), (3948, 0.0), (3950, 0.0), (3964, 0.0), (3965, 0.0), (3968, 0.0), (3969, 0.0), (3971, 0.0), (3972, 0.0), (3977, 0.0), (3979, 0.0), (3980, 0.0), (3981, 0.0), (3982, 0.0), (3985, 0.0), (3988, 0.0), (3991, 0.0), (3994, 0.0), (3996, 0.0), (4003, 0.0), (4006, 0.0), (4010, 0.0), (4018, 0.0), (4021, 0.0), (4022, 0.0), (4026, 0.0), (4027, 0.0), (4029, 0.0), (4031, 0.0), (4034, 0.0), (4037, 0.0), (4040, 0.0), (4041, 0.0), (4058, 0.0), (4063, 0.0), (4065, 0.0), (4067, 0.0), (4070, 0.0), (4072, 0.0), (4073, 0.0), (4078, 0.0), (4084, 0.0), (4086, 0.0), (4097, 0.0), (4100, 0.0), (4108, 0.0), (4109, 0.0), (4112, 0.0), (4114, 0.0), (4115, 0.0), (4125, 0.0), (4127, 0.0), (4131, 0.0), (4144, 0.0), (4146, 0.0), (4150, 0.0), (4153, 0.0), (4157, 0.0), (4159, 0.0), (4166, 0.0), (4167, 0.0), (4168, 0.0), (4170, 0.0), (4173, 0.0), (4179, 0.0), (4180, 0.0), (4181, 0.0), (4185, 0.0), (4186, 0.0), (4188, 0.0), (4190, 0.0), (4191, 0.0), (4194, 0.0), (4198, 0.0), (4199, 0.0), (4201, 0.0), (4204, 0.0), (4207, 0.0), (4212, 0.0), (4214, 0.0), (4215, 0.0), (4218, 0.0), (4223, 0.0), (4224, 0.0), (4229, 0.0), (4234, 0.0), (4237, 0.0), (4238, 0.0), (4239, 0.0), (4241, 0.0), (4250, 0.0), (4253, 0.0), (4256, 0.0), (4258, 0.0), (4260, 0.0), (4270, 0.0), (4271, 0.0), (4276, 0.0), (4278, 0.0), (4279, 0.0), (4291, 0.0), (4297, 0.0), (4300, 0.0), (4302, 0.0), (4305, 0.0), (4313, 0.0), (4315, 0.0), (4316, 0.0), (4317, 0.0), (4319, 0.0), (4323, 0.0), (4324, 0.0), (4327, 0.0), (4329, 0.0), (4332, 0.0), (4338, 0.0), (4341, 0.0), (4346, 0.0), (4347, 0.0), (4352, 0.0), (4353, 0.0), (4358, 0.0), (4364, 0.0), (4370, 0.0), (4372, 0.0), (4393, 0.0), (4404, 0.0), (4405, 0.0), (4406, 0.0), (4408, 0.0), (4410, 0.0), (4413, 0.0), (4414, 0.0), (4415, 0.0), (4417, 0.0), (4421, 0.0), (4424, 0.0), (4425, 0.0), (4433, 0.0), (4434, 0.0), (4437, 0.0), (4439, 0.0), (4447, 0.0), (4449, 0.0), (4451, 0.0), (4453, 0.0), (4454, 0.0), (4455, 0.0), (4457, 0.0), (4460, 0.0), (4463, 0.0), (4478, 0.0), (4480, 0.0), (4483, 0.0), (4485, 0.0), (4491, 0.0), (4493, 0.0), (4496, 0.0), (4498, 0.0), (4499, 0.0), (4500, 0.0), (4506, 0.0), (4508, 0.0), (4509, 0.0), (4519, 0.0), (4525, 0.0), (4526, 0.0), (4532, 0.0), (4539, 0.0), (4541, 0.0), (4542, 0.0), (4547, 0.0), (4549, 0.0), (4556, 0.0), (4558, 0.0), (4559, 0.0), (4560, 0.0), (4561, 0.0), (4562, 0.0), (4565, 0.0), (4568, 0.0), (4569, 0.0), (4570, 0.0), (4577, 0.0), (4578, 0.0), (4580, 0.0), (4592, 0.0), (4597, 0.0), (4599, 0.0), (4600, 0.0), (4609, 0.0), (4613, 0.0), (4615, 0.0), (4618, 0.0), (4622, 0.0), (4628, 0.0), (4631, 0.0), (4635, 0.0), (4644, 0.0), (4647, 0.0), (4648, 0.0), (4651, 0.0), (4654, 0.0), (4655, 0.0), (4662, 0.0), (4667, 0.0), (4671, 0.0), (4672, 0.0), (4675, 0.0), (4676, 0.0), (4681, 0.0), (4683, 0.0), (4688, 0.0), (4690, 0.0), (4700, 0.0), (4702, 0.0), (4711, 0.0), (4714, 0.0), (4716, 0.0), (4720, 0.0), (4725, 0.0), (4728, 0.0), (4730, 0.0), (4736, 0.0), (4737, 0.0), (4740, 0.0), (4741, 0.0), (4742, 0.0), (4745, 0.0), (4750, 0.0), (4751, 0.0), (4754, 0.0), (4755, 0.0), (4758, 0.0), (4759, 0.0)]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print('Top 30 Movies suggested for you : \\n')\n",
        "i = 1\n",
        "for movie in Sorted_Similar_Movies:\n",
        "  index = movie[0]\n",
        "  title_from_index = df[df.index==index]['Movie_Title'].values[0]\n",
        "  if (i<31):\n",
        "    print(i, '.',title_from_index)\n",
        "    i+=1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "s13nrF34Q9sh",
        "outputId": "e6b09790-de0a-4566-ce79-15859c78db70"
      },
      "execution_count": 116,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Top 30 Movies suggested for you : \n",
            "\n",
            "1 . Niagara\n",
            "2 . Caravans\n",
            "3 . My Week with Marilyn\n",
            "4 . Brokeback Mountain\n",
            "5 . Harry Brown\n",
            "6 . Night of the Living Dead\n",
            "7 . The Curse of Downers Grove\n",
            "8 . The Boy Next Door\n",
            "9 . Back to the Future\n",
            "10 . The Juror\n",
            "11 . Some Like It Hot\n",
            "12 . Enough\n",
            "13 . The Kentucky Fried Movie\n",
            "14 . Eye for an Eye\n",
            "15 . Welcome to the Sticks\n",
            "16 . Alice Through the Looking Glass\n",
            "17 . Superman III\n",
            "18 . The Misfits\n",
            "19 . Premium Rush\n",
            "20 . Duel in the Sun\n",
            "21 . Sabotage\n",
            "22 . Small Soldiers\n",
            "23 . All That Jazz\n",
            "24 . Camping Sauvage\n",
            "25 . The Raid\n",
            "26 . Beyond the Black Rainbow\n",
            "27 . To Kill a Mockingbird\n",
            "28 . World Trade Center\n",
            "29 . The Dark Knight Rises\n",
            "30 . Tora! Tora! Tora!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Top 10 Movie Recommendations System"
      ],
      "metadata": {
        "id": "bCiPMWtOVYad"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "Movie_Name = input(' Enter your favourite movie name : ')\n",
        "list_of_all_titles = df['Movie_Title'].tolist()\n",
        "Find_Close_Match = difflib.get_close_matches(Movie_Name, list_of_all_titles)\n",
        "Close_Match = Find_Close_Match[0]\n",
        "Index_of_Movie = df[df.Movie_Title == Close_Match]['Movie_ID'].values[0]\n",
        "Recommendation_Score = list(enumerate(Similarity_Score[Index_of_Movie]))\n",
        "Sorted_Similar_Movies = sorted(Recommendation_Score, key = lambda x:x[1], reverse = True)\n",
        "print('Top 10 Movies suggested for you : \\n')\n",
        "i = 1\n",
        "for movie in Sorted_Similar_Movies:\n",
        "  index = movie[0]\n",
        "  title_from_index = df[df.Movie_ID==index]['Movie_Title'].values\n",
        "  if (i<11):\n",
        "    print(i, '.',title_from_index)\n",
        "    i+=1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3MkZ9cdsQ91x",
        "outputId": "8dd5792e-06c9-4287-d7ec-84613cf6307c"
      },
      "execution_count": 117,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            " Enter your favourite movie name : Avataar\n",
            "Top 10 Movies suggested for you : \n",
            "\n",
            "1 . ['Avatar']\n",
            "2 . ['The Girl on the Train']\n",
            "3 . ['Act of Valor']\n",
            "4 . ['Donnie Darko']\n",
            "5 . ['Precious']\n",
            "6 . ['Freaky Friday']\n",
            "7 . ['The Opposite Sex']\n",
            "8 . ['Heaven is for Real']\n",
            "9 . ['Run Lola Run']\n",
            "10 . ['Elizabethtown']\n"
          ]
        }
      ]
    }
  ]
}