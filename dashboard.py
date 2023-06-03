import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def create_season_df(df):
    season_df = df.groupby(by='season').agg({
    'casual': 'sum',
    'registered': 'sum',
    'cnt': 'sum',
    })

    # season_df.index = pd.Categorical(season_df.index, ["Spring", "Summer", "Fall", "Winter"])

    return season_df

def create_weather_df(df):
    group_by_weather = df.groupby(by='weathersit').agg({
        'casual': 'sum',
        'registered': 'sum',
        'cnt': 'sum',
    })

    return group_by_weather

def create_date_user_df(df):
    df['dteday'] = pd.to_datetime(df['dteday'])
    date_user_df = df.resample('M', on='dteday').sum()[['casual', 'registered', 'cnt']]

    date_user_df.index = date_user_df.index.strftime('%B')
    date_user_df = date_user_df.reset_index()

    return date_user_df

def create_date_user_2011_df(df):
    filter_2011 = df.index <= 11

    date_user_2011_df = df[filter_2011]

    return date_user_2011_df

def create_date_user_2012_df(df):
    filter_2012 = df.index <= 11

    date_user_2012_df = df[filter_2012]

    return date_user_2012_df


day_df = pd.read_csv('bike_data/day.csv')

season_df = create_season_df(day_df)
weather_df = create_weather_df(day_df)
date_user_df = create_date_user_df(day_df)
date_user_2011_df = create_date_user_2011_df(date_user_df)
date_user_2012_df = create_date_user_2012_df(date_user_df)

st.header('Bike Sharing Dashboard :sparkles:')

st.subheader('Jumlah Pengguna Sepeda Berdasarkan Musim')

with st.container():
    colors = ["#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3",]
    fig, ax = plt.subplots(figsize=(16, 8))
    sns.barplot(data=season_df, x=["Spring", "Summer", "Fall", "Winter"], y='cnt', palette=colors)

    ax.set_title("Jumlah Pengguna Berdasarkan Musim", loc="center", fontsize=15)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=12)
    st.pyplot(fig)

st.subheader('Jumlah Pengguna Sepeda Berdasarkan Cuaca')

with st.container():
    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3"]

    fig, ax = plt.subplots(figsize=(16, 8))

    sns.barplot(data=weather_df, x=["Cerah/Berawan", "Berkabut", "Salju/Hujan Ringan"], y='cnt', palette=colors)

    ax.set_title("Jumlah Pengguna Berdasarkan Cuaca", loc="center", fontsize=15)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=12)
    st.pyplot(fig)


st.subheader('Grafik Pengguna Sepeda Tahun 2011 dan 2012 Dalam Setahun')


fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

ax[0].plot(date_user_2011_df['dteday'], date_user_2011_df['casual'], marker='o', linewidth=2, color="#72BCDA", label='Casual')
ax[0].plot(date_user_2011_df['dteday'], date_user_2011_df['registered'], marker='o', linewidth=2, color="#FD8A8A", label='Registered')
ax[0].plot(date_user_2011_df['dteday'], date_user_2011_df['cnt'], marker='o', linewidth=2, color="#829460", label='Total Rentals')
ax[0].set_xticklabels(date_user_2011_df['dteday'], rotation=30, ha='center')
ax[0].set_title("Tahun 2011", loc="center", fontsize=15)
ax[0].legend()

ax[1].plot(date_user_2012_df['dteday'], date_user_2012_df['casual'], marker='o', linewidth=2, color="#72BCDA", label='Casual')
ax[1].plot(date_user_2012_df['dteday'], date_user_2012_df['registered'], marker='o', linewidth=2, color="#FD8A8A", label='Registered')
ax[1].plot(date_user_2012_df['dteday'], date_user_2012_df['cnt'], marker='o', linewidth=2, color="#829460", label='Total Rentals')
ax[1].set_xticklabels(date_user_2012_df['dteday'], rotation=30, ha='center')
ax[1].set_title("Tahun 2012", loc="center", fontsize=15)
ax[1].legend()


plt.suptitle("Grafik Pengguna Sepeda Tahun 2011 dan 2012 Dalam Setahun", fontsize=20)
st.pyplot(fig)


st.subheader('Grafik Pengguna Sepeda Tahun 2011')

colors = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", '#72BCD4',
          "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", '#D3D3D3']

fig, ax = plt.subplots(figsize=(9, 6))
sns.barplot(data=date_user_2011_df, x='dteday', y='cnt', palette=colors)

ax.set_title("Jumlah Pengguna Pada Tahun 2011", loc="center", fontsize=15)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=12)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)

st.subheader('Grafik Pengguna Sepeda Tahun 2012')

colors = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", '#72BCD4',
          "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", '#D3D3D3']

fig, ax = plt.subplots(figsize=(9, 6))
sns.barplot(data=date_user_2012_df, x='dteday', y='cnt', palette=colors)

ax.set_title("Jumlah Pengguna Pada Tahun 2012", loc="center", fontsize=15)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=12)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)


