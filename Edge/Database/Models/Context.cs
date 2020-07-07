using System;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata;

namespace Edge.Database.Models
{
    public partial class Context : DbContext
    {
        public Context()
        {
        }

        public Context(DbContextOptions<Context> options)
            : base(options)
        {
        }

        public virtual DbSet<Settings> Settings { get; set; }
        public virtual DbSet<Stattemperature> Stattemperature { get; set; }
        public virtual DbSet<Temperature> Temperature { get; set; }
        public virtual DbSet<Unitstemperature> Unitstemperature { get; set; }

        /*protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            if (!optionsBuilder.IsConfigured)
            {
#warning To protect potentially sensitive information in your connection string, you should move it out of source code. See http://go.microsoft.com/fwlink/?LinkId=723263 for guidance on storing connection strings.
                optionsBuilder.UseNpgsql("Host=localhost;Database=edge;Username=postgres");
            }
        }*/

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Settings>(entity =>
            {
                entity.HasKey(e => e.HouseName)
                    .HasName("prk_constraint_settings");

                entity.ToTable("settings");

                entity.Property(e => e.HouseName)
                    .HasColumnName("house_name")
                    .HasMaxLength(25);

                entity.Property(e => e.ClimOff).HasColumnName("clim_off");

                entity.Property(e => e.ClimOn).HasColumnName("clim_on");

                entity.Property(e => e.HeatOff).HasColumnName("heat_off");

                entity.Property(e => e.HeatOn).HasColumnName("heat_on");

                entity.Property(e => e.TempUnit).HasColumnName("temp_unit");

                entity.HasOne(d => d.TempUnitNavigation)
                    .WithMany(p => p.Settings)
                    .HasForeignKey(d => d.TempUnit)
                    .HasConstraintName("fk_tempunit_unitstempcode");
            });

            modelBuilder.Entity<Stattemperature>(entity =>
            {
                entity.HasKey(e => e.Statyear)
                    .HasName("prk_constraint_statstemperature");

                entity.ToTable("stattemperature");

                entity.Property(e => e.Statyear)
                    .HasColumnName("statyear")
                    .HasMaxLength(4)
                    .IsFixedLength();

                entity.Property(e => e.Average).HasColumnName("average");

                entity.Property(e => e.ClimDuration).HasColumnName("clim_duration");

                entity.Property(e => e.HeatDuration).HasColumnName("heat_duration");

                entity.Property(e => e.StdDeviation).HasColumnName("std_deviation");
            });

            modelBuilder.Entity<Temperature>(entity =>
            {
                entity.HasKey(e => e.Timer)
                    .HasName("prk_constraint_temperature");

                entity.ToTable("temperature");

                entity.Property(e => e.Timer)
                    .HasColumnName("timer")
                    .HasColumnType("timestamp with time zone");

                entity.Property(e => e.ClimOn).HasColumnName("clim_on");

                entity.Property(e => e.HeatOn).HasColumnName("heat_on");

                entity.Property(e => e.Val).HasColumnName("val");
            });

            modelBuilder.Entity<Unitstemperature>(entity =>
            {
                entity.HasKey(e => e.Code)
                    .HasName("prk_constraint_unitstemperature");

                entity.ToTable("unitstemperature");

                entity.Property(e => e.Code)
                    .HasColumnName("code")
                    .ValueGeneratedNever();

                entity.Property(e => e.Nom)
                    .HasColumnName("nom")
                    .HasMaxLength(25);
            });

            OnModelCreatingPartial(modelBuilder);
        }

        partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
    }
}
